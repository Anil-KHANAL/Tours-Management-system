

let signup= document.querySelector("#form");
if(signup != null){
    signup.addEventListener('submit', e=>{
        e.preventDefault();
        let uname= document.querySelector("#uname").value;
        let pass= document.querySelector("#pass").value;
        let email= document.querySelector("#email").value;
        

        
        let signup = new Signup(uname, pass, email);
        signup.signup();
   
        e.target.reset();
    });

}

const login =document.querySelector('#login');
if(login != null){
    login.addEventListener('submit', e=>{
        e.preventDefault();
        let uname= document.querySelector("#uname").value;
        let pass= document.querySelector("#pass").value;
  
        
        let login =new Login(uname,pass);
     login.login();
   
        e.target.reset();
    });
    
}