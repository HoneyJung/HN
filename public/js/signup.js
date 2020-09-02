function myfunction(){
    console.log("hi")
    console.log(name.value)
    console.log(document.getElementsByName("name").value);
}
    // var form = new FormData(document.getElementById("form"));
    // var inputValue = form.get("pwd");
//     // console.log(inputValue)
//     const mariadb = require('mariadb');
//     const conn = mariadb.createConnection({host: 'localhost', user:'root', password: 'jenjen21c'});
//     conn.query("SELECT * from user_info", (err, rows) => {
//         console.log(rows); //[ {val: 1}, meta: ... ]
//         conn.query("INSERT INTO myTable value (?, ?)", [1, "mariadb"], (err, res) => {
//         console.log(res); // { affectedRows: 1, insertId: 1, warningStatus: 0 }
//         conn.end();
//         });
//     });
// }