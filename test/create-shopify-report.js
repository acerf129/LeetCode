
const converter = require('json-2-csv');
var mysql = require('mysql');
const prompts = require('prompts');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "demo"
  });
function connect_query(groupBy,time_granularity,metric_type){
  sql="";
  var query = con.query(`
SELECT SUM(o.quantity) as quantity,DATE_FORMAT (orders.created_at,'%Y-%m-%d')as Dates
FROM demo.order_items o 
LEFT JOIN demo.product_variants p ON o.sku=p.sku
LEFT JOIN demo.orders orders ON o.order_id=orders.id
GROUP BY DATE_FORMAT (orders.created_at,'%Y-%m-%d')
ORDER BY Dates 
  `,
  
  [time_granularity.date ,groupBy.value, time_granularity.value, metric_type.value], function (error, results) {
    if (error) throw error;
    return results
  });
 
}
con.connect(function(err) {
    if (err) throw err;
  

    con.query(sql1, function (err, result, fields) {
      if (err) throw err;
      console.log(result);
    });
  });
const prompts = require('prompts');

async function run() {


  const groupBy = await prompts([
    {
      type: 'select',
      name: 'type',
      message: 'Group by options',
      choices: [
        {title: 'None', value: 'none'},
        {title: 'SKU', value: 'sku'},
        {title: 'Product name', value: 'product_name'}
      ]
    },
    
  ]);
  const time_granularity = await prompts([
    {
      type: 'select',
      name: 'type',
      message: 'Time granularity',
      choices: [
        {title: 'Daily',date:"DATE_FORMAT(o.created_at,'%Y-%m-%d') as created_at", value: "DATE_FORMAT(o.created_at,'%Y-%m-%d')"},
        {title: 'Monthly',date:"DATE_FORMAT(o.created_at,'%Y-%m') as created_at", value: "DATE_FORMAT(o.created_at,'%Y-%m')"}
      ]
    },
  ]);
  const metric_type = await prompts([
    {
      type: 'select',
      name: 'type',
      message: 'Report metric type',
      choices: [
        {title: 'Gross sales unit', value: 'unit'},
        {title: 'Gross sales amount', value: 'amount'}
      ]
    },
    
  ]);
  json=connect_query(groupBy,time_granularity,metric_type);
  return [json,groupBy.value, time_granularity.value, metric_type.value];
}

run()
  .then((req) => converter.json2csv(req, (err, csv) => {
    if (err) {
        throw err;
    }
    var name=csv[1].val+csv[2].val+csv[3].val;
    fs.writeFileSync(`${name}.csv`,csv[0]);
}))
  .catch((e) => console.log( e));