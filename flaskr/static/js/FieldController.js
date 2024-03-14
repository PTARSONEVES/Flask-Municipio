class FieldController{

    constructor(){
        this._locale = 'pt-BR';
        this._userNameEl = document.querySelector("#user");
        this._dateEl = document.querySelector("#date");
        this._timeEl = document.querySelector("#time");
        this._userPasswordEl = document.querySelector("#password");
        this._userEmailEl = document.querySelector("#email"); 
        this._userName;
        this._userEmail;
        this._userPassword;
        this._currentDate;
        this._formName;
        this.initialize();
    }

    initialize(){
        setInterval(()=>{

            this._dateEl.innerHTML = this.currentDate.toLocaleDateString(this._locale);
            this._timeEl.innerHTML = this.currentDate.toLocaleTimeString(this._locale);

        },1000)
    }

    get userName(){
        return this._userName;
    }

    set userName(value){
        this._userName=value;
    }

    get userEmail(){
        return this._userEmail;
    }

    set userEmail(value){
        this._userEmail=value;
    }

    get userPassword(){
        return this._userPassword;
    }

    set userPassword(value){
        this._userPassword=value;
    }

    get currentDate(){
        return new Date();
    }

    set currentDate(value){
        this._currentDate=value;
    }

    get formName(){
        return this._formName;
    }

    set formName(value){
        this._formName=value;
    }
}