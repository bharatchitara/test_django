
  function emailcheck(){
    var inputText  = document.getElementById("username");
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(inputText.value.match(mailformat))
    {
      
    document.getElementById("username").style.transition = "";
    document.getElementById("username").style.boxShadow = "";
    document.getElementById("help1").style.display = "none";
    document.getElementById("submit").disabled=false;
      return true;
    }
    else
    {
    //document.getElementById("username").style.border = "solid red";
    
    
    document.getElementById("username").style.transition = "box-shadow linear 1s";
    document.getElementById("username").style.boxShadow = "0 0 20px red";
    document.getElementById("help1").style.display = "";
    document.getElementById("submit").disabled=true;
    return true;
    }
  }


  function passwdcheck(){
   var inputpasswd = document.getElementById("passwd");
   var passwd_regex =  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%#*?&])[A-Za-z\d@$!%#*?&]{8,}$/;



   if(inputpasswd.value.match(passwd_regex)){
     //console.log("paass")
    
    document.getElementById("passwd").style.transition = "";
    document.getElementById("passwd").style.boxShadow = "";
    document.getElementById("help2").style.display = "none";
    document.getElementById("submit").disabled=false;
    return true;
   }
   else{
    //console.log("paass")

    document.getElementById("passwd").style.transition = "box-shadow linear 1s";
    document.getElementById("passwd").style.boxShadow = "0 0 20px red";
    document.getElementById("help2").style.display = "";
    document.getElementById("submit").disabled=true;
    return true;


   }

  }

  function enablepwd(){
    var x = document.getElementById("passwd");
  if (x.type == "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
