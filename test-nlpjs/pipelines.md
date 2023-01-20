# default

## main
nlp.train

## onIntent(gurbani.random)
// compiler=javascript
const shabad = request.get('https://api.banidb.com/v2/random');

if (shabad && shabad.shabadInfo && shabad.shabadInfo.shabadId) {
    input.answer = "It is a blessed day to immerse in Gurbani https://www.sikhitothemax.org/shabad?random OR https://api.banidb.com/v2/shabads/" + shabad.shabadInfo.shabadId;
}



# main
console.say "Say something!"

## console.hear
// compiler=javascript
if (message === 'quit') {
  return console.exit();
}
nlp.process();
this.say();
