export default class Currency {
  constructor(code, name) {
    if (typeof (name) === 'string') { this._name = name; }
    if (typeof (code) === 'string') { this._code = code; }
  }

  set name(name) {
    if (typeof (name) === 'string') { this._name = name; }
  }

  get name() {
    return this._name;
  }

  set code(code) {
    if (typeof (code) === 'string') { this._code = code; }
  }

  get code() {
    return this._code;
  }

  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}
