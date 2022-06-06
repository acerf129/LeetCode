function resolveAfter2Seconds(){
    console.log("starting slow promise");
    return new Promise(resolve=>{
        setTimeout(()=>{
            resolve("slow");
        },2000)
    });
}
function resolveAfter1Second(){
    console.log("starting fast promise");
    return new Promise(resolve=>{
        setTimeout(()=>{
            resolve("fast");
        },1000)
    })
}
async function sequentialStart(){
    console.log("Sequential: start");
    const slow = await resolveAfter2Seconds();
    console.log("slow");//after 2 scrond
    const fast = await resolveAfter1Second();
    console.log("fast");//after 3 second
}
async function concurrentStart(){
    console.log("ConcurrentStart: start");
    const slow =  resolveAfter2Seconds();
    const fast =  resolveAfter1Second();
    console.log(await slow);//after two second
    console.log(await fast);//after two second
}
//sequentialStart();
//concurrentStart()

function concurrentPromise() {
    console.log('==CONCURRENT START with Promise.all==')
    return Promise.all([resolveAfter2Seconds(), resolveAfter1Second()]).then((messages) => {
      console.log(messages[0]) // slow
      console.log(messages[1]) // fast
    })
  }
  
  async function parallel() {
    console.log('==PARALLEL with await Promise.all==')
  
    // Start 2 "jobs" in parallel and wait for both of them to complete
    await Promise.all([
        (async()=>console.log(await resolveAfter2Seconds()))(),
        (async()=>console.log(await resolveAfter1Second()))()
    ])
  }
  
  // wait 3 second start two promise return at 2 second then
  setTimeout(concurrentPromise, 3000) // same as concurrentStart
