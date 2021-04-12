 
 class User{
     constructor(uname,pass){
        this.username = uname;
        this.password = pass;
    
     }

     makeData(){
         let data={
            username: this.username,
            password: this.password,
            email: this.email,
        
         };
         return data;
        }
     checkLogin(args){
        if(args.length>0){
            return true;

        }else{
            return false;}
     }

 }