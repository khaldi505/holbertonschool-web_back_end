import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, Currency){
        if (typeof(Currency) === "object") { this._Currency = Currency }
        if (typeof(amount) == "number") {this._amount = amount}
    }
    static convertPrice(amount, conversionRate ){
        return amount * conversionRate
    }
    set amount(amount) {
        if (typeof(amount) === 'number') { this._amount = amount }
      }
    
      get amount() {
        return this._amount
      }
    
      set Currency(Currency) {
        if (typeof(Currency) === 'object') { this._Currency = Currency }
      }
    
      get Currency() {
        return this._Currency
      }
      displayFullPrice(){
        return (`${this._amount} ${this.Currency._name} (${this.Currency._code})`)
      }
}
