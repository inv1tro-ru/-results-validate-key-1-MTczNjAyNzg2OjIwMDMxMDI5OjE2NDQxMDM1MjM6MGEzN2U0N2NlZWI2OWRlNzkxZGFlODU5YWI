
(function (ph){
try{
var A = self['DSPCounter' || 'AdriverCounter'], 
	a = A(ph);
a.reply = {
ph:ph,
rnd:'273416',
bt:62,
sid:222906,
pz:0,
sz:'%2f',
bn:0,
sliceid:0,
netid:0,
ntype:0,
tns:0,
pass:'',
adid:0,
bid:2864425,
geoid:81,
cgihref:'//ad.adriver.ru/cgi-bin/click.cgi?sid=222906&ad=0&bid=2864425&bt=62&bn=0&pz=0&xpid=DlEB89woB4kb1nvcWG1-5OE_YOsnZS-uGvEa5H1f6wqUdIJRVgELRqT9S9qhRmuFD_WM7jfYf&ref=https:%2f%2fwww.invitro.ru%2f&custom=157%3D2079199115.1635843391%3B158%3D%25D0%25A1%25D0%25B0%25D1%2580%25D0%25B0%25D1%2582%25D0%25BE%25D0%25B2%3B206%3DDSPCounter',
target:'_blank',
width:'0',
height:'0',
alt:'AdRiver',
mirror:A.httplize('//servers1.adriver.ru'), 
comp0:'0/script.js',
custom:{"157":"2079199115.1635843391","158":"%D0%A1%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2","206":"DSPCounter"},
cid:'',
uid:0,
xpid:'DlEB89woB4kb1nvcWG1-5OE_YOsnZS-uGvEa5H1f6wqUdIJRVgELRqT9S9qhRmuFD_WM7jfYf'
}
var r = a.reply;

r.comppath = r.mirror + '/images/0002864/0002864425/' + (/^0\//.test(r.comp0) ? '0/' : '');
r.comp0 = r.comp0.replace(/^0\//,'');
if (r.comp0 == "script.js" && r.adid){
	A.defaultMirror = r.mirror; 
	A.loadScript(r.comppath + r.comp0 + '?v' + ph) 
} else if ("function" === typeof (A.loadComplete)) {
   A.loadComplete(a.reply);
}
(function (o) {
	var i, w = o.c || window, d = document, y = 10;
	function oL(){
		if (!w.postMessage || !w.addEventListener) {return;}
		if (w.document.readyState == 'complete') {return sL();}
		w.addEventListener('load', sL, false);
	}
	function sL(){try{i.contentWindow.postMessage('pgLd', '*');}catch(e){}}
	function mI(u, oL){
		var i = d.createElement('iframe'); i.setAttribute('src', o.hl(u)); i.onload = oL; with(i.style){width = height = '10px'; position = 'absolute'; top = left = '-10000px'} d.body.appendChild(i);
		return i;
	}
	function st(u, oL){
		if (d.body){return i = mI(u, oL)}
		if(y--){setTimeout(function(){st(u, oL)}, 100)}
	}
	st(o.hl('https://content.adriver.ru/banners/0002186/0002186173/0/l6.html?0&0&1&0&273416&0&0&81&78.106.45.90&counter&' + (o.all || 0)), oL);
}({
	hl: A.httplize,
	
	all: 1
	
}));
}catch(e){} 
}('0'));
