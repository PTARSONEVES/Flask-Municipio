class FieldController{

    constructor(){
        this._locale = 'pt-BR';
        this._userNameEl = document.querySelector("#user");
        this._dayEl = document.querySelector("#day");
        this._dateEl = document.querySelector("#date");
        this._timeEl = document.querySelector("#time");
        this._userPasswordEl = document.querySelector("#password");
        this._userEmailEl = document.querySelector("#email"); 
        this._currentDate;
        this._formName;
        this.initialize();
        this.initInputEvents();
    }

    initialize(){
        this.setDateTime(this._locale,"long");
        setInterval(()=>{
            this.setDateTime();
        },1000);
    }

    addEventListenerAll(element, events, fn){

        events.split(',').forEach(event => {
            console.log(event);
            element.addEventListener(event, fn,false);
        });

    }

    initInputEvents(){
        let element = "input";
        let elements = document.querySelectorAll(element);
        elements.forEach(element=>{
            this.addEventListenerAll(element,"click,drag", e => {
                console.log(element.name);
            });
        });

        this.addEventListenerAll(element, "mouseover,mouseup,mousedown", e => {
            element.style.cursor = "pointer";
        });
    }

    setWeekday(type){
        var weekday=[];
        switch(this._locale){
            case 'pt-BR':
                if (type === "long"){
                    weekday = ["Domingo","Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado"];
                } else {
                    weekday = ["Dom","Seg","Ter","Qua","Qui","Sex","Sáb"]
                }
                break;
            default:
                if (type === "long"){
                    weekday = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"];
                } else {
                    weekday = ["Sun","Mon","Tue","Wed","Thr","Fri","Sat"]
                }
                break;
        }
        return weekday[this.currentDate.getDay()];
    }

    setDateTime(){
        this._dayEl.innerHTML = this.setWeekday();
        this._dateEl.innerHTML = this.currentDate.toLocaleDateString(this._locale);
        this._timeEl.innerHTML = this.currentDate.toLocaleTimeString(this._locale);
    }

    get userName(){
        return this._userNameEl.innerHTML;
    }

    set userName(value){
        this._userNameEl.innerHTML=value;
    }

    get userEmail(){
        return this._userEmailEl.innerHTML;
    }

    set userEmail(value){
        this._userEmailEl.innerHTML=value;
    }

    get userPassword(){
        return this._userPasswordEl.innerHTML;
    }

    set userPassword(value){
        this._userPasswordEl.innerHTML=value;
    }

    get currentDate(){
        return new Date();
    }

    set currentDate(value){
        this._currentDate=value;
    }

    get day(){
        return this._dayEl.innerHTML;
    }

    set day(value){
        this._dayEl.innerHTML=value;
    }

    get date(){
        return this._dateEl.innerHTML;
    }

    set date(value){
        this._dateEl.innerHTML=value;
    }

    get time(){
        return this._timeEl.innerHTML;
    }

    set time(value){
        this._timeEl.innerHTML=value;
    }

    get formName(){
        return this._formName;
    }

    set formName(value){
        this._formName=value;
    }
}