
console.log("this is")
const flag_button = document.getElementById("issue");

console.log(flag_button.length)

const get_book_id = document.getElementsByName("book_id");
const uname_from_Locstorage = localStorage.getItem("user");

console.log(get_book_id)
    
            for(let i = 0; i<flag_button.length; i++){
                 flag_button[i].addEventListener("click", ()=>{
                     console.log("this is")
    
                    if(flag_button[i].value == "Issue"){
                        console.log(get_book_id[i].value)
                        
                        
                        
                    

                        $.ajax({
                            type: "GET",
                            url: 'test_book_allocate/',
                            data: {
                                "getbookid": get_book_id[i].value,
                                "uname_local":uname_from_Locstorage

                                
                            },
                            dataType: "json",
                            success: function (data) {

                                if(data["flag"] == 1 ){
                                  alert("Either requested book is already allocated or the student already have 3 books allocated!");

                                }
                                else{

                                alert("Book is issued!")
                                }
                            },
                            failure: function () {

                                alert("Either requested book is already allocated or the student already have 3 books allocated!");
                            }
                        });

                        if(data["flag"] == 0 ){
                        flag_button[i].value = "Allocated";
                        flag_button[i].disabled = true;
                        }  

    
    
                        }
                    
            });
    
                } 
                
              



