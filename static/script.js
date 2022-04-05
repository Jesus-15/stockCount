function getInventory(){
    let url = "/read";
    let jsonhttp = new XMLHttpRequest();
    let response = "ERROR occurred while getting journal entries";

  jsonhttp.onreadystatechange = function () {
      if (this.readyState === 4) {
          if (this.status === 200) {
              response = JSON.parse((this.responseText));
              let inventoryEntries = JSON.parse(response.result)
              // console.log(inventoryEntries);
              let inventoryAll = inventoryEntries.inventory; // Array
              // console.log(inventoryAll);
              let inventoryList = ""
              let row = 1
              let table = "";

              for (let i = 0; i < inventoryAll.length; i++) {

                  var idInput = "count" + (i + 1);
                  var input = "<input type='text' class='form-control' placeholder='Counts' id='"+idInput+"'>";
                  var arr = inventoryAll[i];
                  var idButton = "btnSend" + (i + 1);
                  var button = "<button type='button' class='btn btn-outline-success' onclick='countDone(this)' id='"+idButton+"'>Send</button>";

                  var idSku = "sku" + (i + 1);
                  var idCount = "count" + (i + 1);
                  // console.log(arr);

                  var tr = "<tr>";
                  tr += "<th id='row'>" + row + "</th>";
                  tr += "<td id="+idSku+">" + inventoryAll[i]["sku"] + "</td>";
                  tr += "<td id='description'>" + inventoryAll[i]["description"] + "</td>";
                  tr += "<td id='location'>" + inventoryAll[i]["location"] + "</td>";
                  tr += "<td id='"+idCount+"'>" + input + "</td>";
                  tr += "<td id='button'>" + button +"</td>";
                  tr += "</tr>";
                  table += tr;
                  row++;

              }
              document.getElementById("inventoryTable").innerHTML += table;
          }
      }
  };
  jsonhttp.open("GET", url, true);
  jsonhttp.send();
}
getInventory();

function countDone(x) {
    let url = "/read"
    let counthttp = new XMLHttpRequest();
    let response = "ERROR occurred while getting journal entries";

    counthttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                response = JSON.parse((this.responseText));
                let inventoryEntries = JSON.parse(response.result)
                // console.log(inventoryEntries);
                let inventoryAll = inventoryEntries.inventory; // Array
                // console.log(x.id);

                for (let i = 0; i < inventoryAll.length; i++) {

                    var id = "btnSend" + (1 + i);
                    // console.log(inventoryAll[i]);
                    if(x.id === id){
                        console.log(inventoryAll[i]);
                        // console.log("test");
                    }
                    // if(x == "btnSend" + i){
                    //     let y = inventoryAll[i];
                    //     return y;
                    // }

                }
                // document.getElementById("test2").innerHTML = y;
            }
            // console.log(x);
        }
    };
    counthttp.open("GET", url, true);
    counthttp.send();
}

function callAPI(url, elResponse) {
    //use the code from the lab task to complete the function
    let xhttp = new XMLHttpRequest();
    let response = "Error no response";

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            response = JSON.parse(this.responseText);
        }
        document.getElementById(elResponse).setAttribute("value", response.result);
    }
    xhttp.open("GET", url, true);
    xhttp.send();
}

function delFunction(){
    var x = document.getElementById("inventoryTable").rows[1];
    var sku = document.getElementById("sku1");
    var count = document.getElementById("count1");
    var td = document.getElementsByTagName("td");
    var url = "/api/add?sku=" + sku + "&count=" + count;
    console.log(sku);
    console.log(url);
    console.log(x);
    console.log(td);
}
delFunction();