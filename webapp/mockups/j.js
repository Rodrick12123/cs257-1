function valGetter() {  
    alert("Choose sth")

    // const years = new Array();
    let years = [];
    var all = document.getElementById("allc");  
    var v1 = document.getElementById("1930");  
    var v2 = document.getElementById("1934");
    var v3 = document.getElementById("1938");
    var v4 = document.getElementById("1950");
    var v5 = document.getElementById("1954");
    var v6 = document.getElementById("1958");
    var v7 = document.getElementById("1962");
    var v8 = document.getElementById("1966");
    var v9 = document.getElementById("1970");
    var v10 = document.getElementById("1974");
    var v11 = document.getElementById("1978");
    var v12= document.getElementById("1982");
    var v13 = document.getElementById("1986");
    var v14 = document.getElementById("1990");
    var v15= document.getElementById("1994");
    var v16= document.getElementById("1998");
    var v17 = document.getElementById("2002");
    var v18 = document.getElementById("2006");
    var v19 = document.getElementById("2010");
    var v20 = document.getElementById("2014");
    
    if (all.checked == true){  
        // return document.getElementById("error").innerHTML = "Please mark only one checkbox either Yes or No"; 
        window.location.href="C:\Users\rodri\cs257\257\cs257\cs257\webapp\mockups\mockup3.html"; 
    }
    else{
        if (v1.checked == true){  
            var a = document.getElementById("1930").value;  
            // return document.getElementById("result").innerHTML = y; 
            years.push(a)  
        }
        if (v2.checked == true){  
            var b = document.getElementById("1934").value;  
            // return document.getElementById("result").innerHTML = y; 
            years.push(b)  
        }
        if (v3.checked == true){  
            var c = document.getElementById("1938").value;  
            // return document.getElementById("result").innerHTML = y; 
            years.push(c)  
        }
        if (v4.checked == true){  
            var d = document.getElementById("1950").value;  
            years.push(d)  
        }
        if (v5.checked == true){  
            var e = document.getElementById("1954").value;  
            years.push(e)  
        }
        if (v6.checked == true){  
            var f = document.getElementById("1958").value;  
            years.push(f)  
        }
        if (v7.checked == true){  
            var g = document.getElementById("1962").value;  
            years.push(g)  
        }
        if (v8.checked == true){  
            var h = document.getElementById("1966").value;  
            years.push(h)  
        }
        if (v9.checked == true){  
            var i = document.getElementById("1970").value;  
            years.push(i)  
        }
        if (v10.checked == true){  
            var j = document.getElementById("1974").value;  
            years.push(j)  
        }
        if (v11.checked == true){  
            var k = document.getElementById("1978").value;  
            years.push(k)  
        }
        if (v12.checked == true){  
            var l = document.getElementById("1982").value;  
            years.push(l)  
        }
        if (v13.checked == true){  
            var m = document.getElementById("1986").value;  
            years.push(m)  
        }
        if (v14.checked == true){  
            var n = document.getElementById("1990").value;  
            years.push(o)  
        }
        if (v15.checked == true){  
            var p = document.getElementById("1994").value;  
            years.push(p)  
        }
        if (v16.checked == true){  
            var q = document.getElementById("1998").value;  
            years.push(q)  
        }
        if (v17.checked == true){  
            var r = document.getElementById("2002").value;  
            years.push(r)  
        }
        if (v18.checked == true){  
            var s = document.getElementById("2006").value;  
            years.push(s)  
        }
        if (v19.checked == true){  
            var t = document.getElementById("2010").value;  
            years.push(t)  
        }
        if (v20.checked == true){  
            var u = document.getElementById("2014").value;  
            years.push(u)  
        }
    }
    if (years.length != 0 && all.checked == false){
        window.location.href="C:\Users\rodri\cs257\257\cs257\cs257\webapp\mockups\mockup2.html";
        
    }
    else{
        //return document.getElementById("error").innerHTML = "Please mark choose a World Cup year";
        alert("You Must Select Something")
    }
}