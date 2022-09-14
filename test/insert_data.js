var mysql = require('mysql');
var express=require('express');
var https=require('https');
var app=express();
const cors=require('cors');
app.use(cors({origin:'*'}));

let url1 = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1861ba94-f601-4858-919d-f768dd44dae2/orders.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220901T025127Z&X-Amz-Expires=86400&X-Amz-Signature=5c185e087f9b81046a55092809b8bb99352c6ad4b89bbd98c4b16d054f1eb138&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22orders.json%22&x-id=GetObject";
let url2="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/48ecca56-1fbb-4fbf-ad14-1168be9c2bbf/products.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220901T025157Z&X-Amz-Expires=86400&X-Amz-Signature=c5d4507f0f2fba2b992e2237c7b43761e5dd47f43ed52b4c5c8fa04573c1479b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22products.json%22&x-id=GetObject";
var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "demo",
    port:3306
  });
https.get(url1,function(res){
    let body="";
    res.on('data',function(chunk){
        body+=chunk;
    })
    res.on('end',function(){
        try{
            let json=JSON.parse(body);
            insertData(json.data,"order");
        }catch(err){
            console.log(err);
        };       
    });       
}).on('error',function(e){
    console.log("Error",e);
});
https.get(url2,function(res){
    let body="";
    res.on('data',function(chunk){
        body+=chunk;
    })
    res.on('end',function(){
        try{
            let json=JSON.parse(body);
            //insertData(json.data,"product");
        }catch(err){
            console.log(err);
        };       
    });       
}).on('error',function(e){
    console.log("Error",e);
});
function insertData(json,table){
    con.connect(function(err) {
        if (err) throw err;
        n=json.length;
        if (table=="order")
        {
            for(var i=0;i<n;i++){
                id=json[i].id;
                order_number=json[i].order_number;
                financial_status=json[i].financial_status;
                subtotal_price=parseFloat(json[i].subtotal_price);
                total_price=parseFloat(json[i].total_price);
                total_tax=parseFloat(json[i].total_tax);
                date=new Date(json[i].created_at);
                created_at=date.toISOString().slice(0, 19).replace('T', ' ');
                date=new Date(json[i].updated_at);
                updated_at=date.toISOString().slice(0, 19).replace('T', ' ');
                let values=[id,order_number,financial_status,created_at,subtotal_price,total_price,total_tax,updated_at];
                var sql =`INSERT INTO orders(id,order_number,financial_status,created_at,subtotal_price,total_price,total_tax,updated_at) VALUES( ?)`;
                con.query(sql,[values], function (err, result) {
                    if (err) throw err;
                });
                nitems=json[i].line_items.length;
                for(var j=0;j<nitems;j++){
                    id=json[i].line_items[j].id;
                    order_id=json[i].line_items[j].order_id;
                    quantity=parseInt(json[i].line_items[j].quantity);
                    sku=json[i].line_items[j].sku;
                    price=parseFloat(json[i].line_items[j].price);
                    shop_money_amount=parseFloat(json[i].line_items[j].price_set.shop_money.amount);
                    shop_money_code=json[i].line_items[j].price_set.shop_money.currency_code;
                    let values=[id,order_id,quantity,sku,price,shop_money_amount,shop_money_code];
                    var sql =`INSERT INTO order_items(id,order_id,quantity,sku,price,shop_money_amount,shop_money_code) VALUES( ?)`;
                    con.query(sql,[values], function (err, result) {
                    if (err) throw err;
                });
                };
            };
        }
        else if (table=="product"){
            for(var i=0;i<n;i++){
                id=json[i].id;
                title=json[i].title;
                vendor=json[i].vendor;
                date=new Date(json[i].created_at);
                created_at=date.toISOString().slice(0, 19).replace('T', ' ');

                product_type=json[i].product_type;
                let values=[id,title,vendor,created_at,product_type];
                var sql =`INSERT INTO products(id,title,vendor,created_at,product_type) VALUES( ? )`;
                con.query(sql,[values], function (err, result) {
                    if (err) throw err;
                });
                nitems=json[i].variants.length;
                for(var j=0;j<nitems;j++){
                    id=json[i].variants[j].id;
                    product_id=json[i].variants[j].product_id;
                    title=json[i].variants[j].title;
                    price= parseFloat(json[i].variants[j].price);
                    sku=json[i].variants[j].sku;    
                    date=new Date(json[i].variants[j].created_at);
                    created_at=date.toISOString().slice(0, 19).replace('T', ' ');

                    let values=[id,product_id,title,price,sku,created_at];
                    var sql =`INSERT INTO product_variants(id,product_id,title,price,sku,created_at) VALUES( ? )`;
                    con.query(sql,[values], function (err, result) {
                    if (err) throw err;
                });
                };
            };
        }
        console.log("Completed");
      });
}
// app.get('/',(req,res)=>{
    
// })
// app.listen(3000,(req,res)=>{
//     console.log("Listening 3000port");
// })