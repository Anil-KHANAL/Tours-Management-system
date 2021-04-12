 class Signup extends User{
     constructor(uname,pass, email){
        super (uname, pass);
        this.email= email;
        

     }

     signup(){
         const data= this.makeData();
         axios.post('http://localhost:3000/users',data)
         .then(res => {
             console.log("user signed up");
         }).catch(e=> console.log(e));
     }

}