var $threeIdeas = $('h2:contains("3 Ideas From Me"):first').parent();
var $twoQuotes = $('h2:contains("2 Quotes From Others"):first').parent();
var $oneQuestion = $('h2:contains("1 Question For You"):first').parent();
var $body = $oneQuestion.parent();
var $hrs = $body.find('hr');
var $enjoythat = $('p:contains("If you enjoyed that")')


function eleToText(arrayObj) {
  var result = ''
  arrayObj.each( (_, ele) => {
    var $ele = $(ele);
    if ( $ele.text().trim().length > 0 && !$(ele).text().includes('Twitter') ) {
      result += '\n' + $ele.text() + '\n';
    }
	});
	return result;
}


var aaaa = $threeIdeas.next().nextUntil($hrs[0]);
var bbbb = $($hrs[0]).next().nextUntil($hrs[1]);
var cccc = $($hrs[1]).next().nextUntil($twoQuotes);

var dddd = $twoQuotes.next().nextUntil($hrs[2]);
var eeee = $($hrs[2]).next().nextUntil($oneQuestion);
var ffff = $oneQuestion.nextUntil($enjoythat);

var aaa = eleToText(aaaa);
var bbb = eleToText(bbbb);
var ccc = eleToText(cccc);
var ddd = eleToText(dddd);
var eee = eleToText(eeee);
var fff = eleToText(ffff);

ideas.push(aaa);
ideas.push(bbb);
ideas.push(ccc);
quotes.push(ddd);
quotes.push(eee);
questions.push(fff);


for ( let i = ideas.length - 3; i < ideas.length ; i++ ) {
  console.log(ideas[i]);
}
for ( let i = quotes.length - 2; i < quotes.length ; i++ ) {
  console.log(quotes[i]);
}
console.log(questions[questions.length-1]);

var ideas = [];
var quotes = [];
var questions = [];