export default class Building {
constructor(sqft){
if (this.constructor !== Building && !this.evacuationWarningMessage) throw Error('Class extending Building must override evacuationWarningMessage');
if (typeof(sqft) !== "number") { this._sqft = sqft }

}
get sqft(){
return this._sqft
}
set sqft(sqft){
if (typeof(sqft) !== "number") { this._sqft = sqft }
}

}
