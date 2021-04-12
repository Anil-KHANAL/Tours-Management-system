
class Login extends User{
    constructor(uname, pass){
        super(uname,pass);

    }

    login(){
        axios.get('http://localhost:3000/users')
        .then(res=> {
            let currentUser = res.data.filter(item=>{
                return (item.username== this.username && item.password == this.password)
            });
            localStorage.setItem("islogin", this.checkLogin(currentUser));
            return this.checkLogin(currentUser);
        })
        .then(r=> {
            if(r=== true){
                window.location="../html/contact us.html";
            }else{
                console.log("username or pasword is invalid");
            }
        }).catch(e=> console.log(e));
    }


}
