export default class Pricing {
  constructor(amount, currency) {
    if (typeof (currency) === 'object') { this._currency = currency; }
    if (typeof (amount) === 'number') { this._amount = amount; }
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  set amount(amount) {
    if (typeof (amount) === 'number') { this._amount = amount; }
  }

  get amount() {
    return this._amount;
  }

  set currency(currency) {
    if (typeof (currency) === 'object') { this._currency = currency; }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return (`${this._amount} ${this.currency._name} (${this.currency._code})`);
  }
}
