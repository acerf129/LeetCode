(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[2015],{19313:function(t,e,n){var i=n(89703);function r(){return(r=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var n=arguments[e];for(var i in n)Object.prototype.hasOwnProperty.call(n,i)&&(t[i]=n[i])}return t}).apply(this,arguments)}var s=i.createElement("svg",{viewBox:"-2 -5 14 20",height:"100%",width:"100%",style:{position:"absolute",top:0}},i.createElement("path",{d:"M9.9 2.12L7.78 0 4.95 2.828 2.12 0 0 2.12l2.83 2.83L0 7.776 2.123 9.9 4.95 7.07 7.78 9.9 9.9 7.776 7.072 4.95 9.9 2.12",fill:"#fff",fillRule:"evenodd"})),o=i.createElement("svg",{height:"100%",width:"100%",viewBox:"-2 -5 17 21",style:{position:"absolute",top:0}},i.createElement("path",{d:"M11.264 0L5.26 6.004 2.103 2.847 0 4.95l5.26 5.26 8.108-8.107L11.264 0",fill:"#fff",fillRule:"evenodd"}));function h(t){if(7===t.length)return t;for(var e="#",n=1;n<4;n+=1)e+=t[n]+t[n];return e}function a(t,e,n,i,r){return function(t,e,n,i,r){var s=(t-n)/(e-n);if(0===s)return i;if(1===s)return r;for(var o="#",h=1;h<6;h+=2){var a=parseInt(i.substr(h,2),16),f=parseInt(r.substr(h,2),16),l=Math.round((1-s)*a+s*f).toString(16);1===l.length&&(l="0"+l),o+=l}return o}(t,e,n,h(i),h(r))}var f=function(t){function e(e){t.call(this,e);var n=e.height,i=e.width,r=e.checked;this.t=e.handleDiameter||n-2,this.i=Math.max(i-n,i-(n+this.t)/2),this.o=Math.max(0,(n-this.t)/2),this.state={h:r?this.i:this.o},this.l=0,this.u=0,this.p=this.p.bind(this),this.v=this.v.bind(this),this.g=this.g.bind(this),this.k=this.k.bind(this),this.M=this.M.bind(this),this.m=this.m.bind(this),this.T=this.T.bind(this),this.$=this.$.bind(this),this.C=this.C.bind(this),this.D=this.D.bind(this),this.O=this.O.bind(this),this.S=this.S.bind(this)}return t&&(e.__proto__=t),(e.prototype=Object.create(t&&t.prototype)).constructor=e,e.prototype.componentDidMount=function(){this.W=!0},e.prototype.componentDidUpdate=function(t){t.checked!==this.props.checked&&this.setState({h:this.props.checked?this.i:this.o})},e.prototype.componentWillUnmount=function(){this.W=!1},e.prototype.I=function(t){this.H.focus(),this.setState({R:t,j:!0,B:Date.now()})},e.prototype.L=function(t){var e=this.state,n=e.R,i=e.h,r=(this.props.checked?this.i:this.o)+t-n;e.N||t===n||this.setState({N:!0});var s=Math.min(this.i,Math.max(this.o,r));s!==i&&this.setState({h:s})},e.prototype.U=function(t){var e=this.state,n=e.h,i=e.N,r=e.B,s=this.props.checked,o=(this.i+this.o)/2;this.setState({h:this.props.checked?this.i:this.o});var h=Date.now()-r;(!i||h<250||s&&n<=o||!s&&n>=o)&&this.A(t),this.W&&this.setState({N:!1,j:!1}),this.l=Date.now()},e.prototype.p=function(t){t.preventDefault(),"number"==typeof t.button&&0!==t.button||(this.I(t.clientX),window.addEventListener("mousemove",this.v),window.addEventListener("mouseup",this.g))},e.prototype.v=function(t){t.preventDefault(),this.L(t.clientX)},e.prototype.g=function(t){this.U(t),window.removeEventListener("mousemove",this.v),window.removeEventListener("mouseup",this.g)},e.prototype.k=function(t){this.X=null,this.I(t.touches[0].clientX)},e.prototype.M=function(t){this.L(t.touches[0].clientX)},e.prototype.m=function(t){t.preventDefault(),this.U(t)},e.prototype.$=function(t){Date.now()-this.l>50&&(this.A(t),Date.now()-this.u>50&&this.W&&this.setState({j:!1}))},e.prototype.C=function(){this.u=Date.now()},e.prototype.D=function(){this.setState({j:!0})},e.prototype.O=function(){this.setState({j:!1})},e.prototype.S=function(t){this.H=t},e.prototype.T=function(t){t.preventDefault(),this.H.focus(),this.A(t),this.W&&this.setState({j:!1})},e.prototype.A=function(t){var e=this.props;(0,e.onChange)(!e.checked,t,e.id)},e.prototype.render=function(){var t=this.props,e=t.checked,n=t.disabled,s=t.className,o=t.offColor,h=t.onColor,f=t.offHandleColor,l=t.onHandleColor,c=t.checkedIcon,u=t.uncheckedIcon,g=t.checkedHandleIcon,d=t.uncheckedHandleIcon,p=t.boxShadow,b=t.activeBoxShadow,v=t.height,_=t.width,m=t.borderRadius,w=function(t,e){var n={};for(var i in t)Object.prototype.hasOwnProperty.call(t,i)&&-1===e.indexOf(i)&&(n[i]=t[i]);return n}(t,["checked","disabled","className","offColor","onColor","offHandleColor","onHandleColor","checkedIcon","uncheckedIcon","checkedHandleIcon","uncheckedHandleIcon","boxShadow","activeBoxShadow","height","width","borderRadius","handleDiameter"]),y=this.state,M=y.h,x=y.N,k=y.j,D={position:"relative",display:"inline-block",textAlign:"left",opacity:n?.5:1,direction:"ltr",borderRadius:v/2,WebkitTransition:"opacity 0.25s",MozTransition:"opacity 0.25s",transition:"opacity 0.25s",touchAction:"none",WebkitTapHighlightColor:"rgba(0, 0, 0, 0)",WebkitUserSelect:"none",MozUserSelect:"none",msUserSelect:"none",userSelect:"none"},S={height:v,width:_,margin:Math.max(0,(this.t-v)/2),position:"relative",background:a(M,this.i,this.o,o,h),borderRadius:"number"==typeof m?m:v/2,cursor:n?"default":"pointer",WebkitTransition:x?null:"background 0.25s",MozTransition:x?null:"background 0.25s",transition:x?null:"background 0.25s"},E={height:v,width:Math.min(1.5*v,_-(this.t+v)/2+1),position:"relative",opacity:(M-this.o)/(this.i-this.o),pointerEvents:"none",WebkitTransition:x?null:"opacity 0.25s",MozTransition:x?null:"opacity 0.25s",transition:x?null:"opacity 0.25s"},O={height:v,width:Math.min(1.5*v,_-(this.t+v)/2+1),position:"absolute",opacity:1-(M-this.o)/(this.i-this.o),right:0,top:0,pointerEvents:"none",WebkitTransition:x?null:"opacity 0.25s",MozTransition:x?null:"opacity 0.25s",transition:x?null:"opacity 0.25s"},A={height:this.t,width:this.t,background:a(M,this.i,this.o,f,l),display:"inline-block",cursor:n?"default":"pointer",borderRadius:"number"==typeof m?m-1:"50%",position:"absolute",transform:"translateX("+M+"px)",top:Math.max(0,(v-this.t)/2),outline:0,boxShadow:k?b:p,border:0,WebkitTransition:x?null:"background-color 0.25s, transform 0.25s, box-shadow 0.15s",MozTransition:x?null:"background-color 0.25s, transform 0.25s, box-shadow 0.15s",transition:x?null:"background-color 0.25s, transform 0.25s, box-shadow 0.15s"},T={height:this.t,width:this.t,opacity:Math.max(2*(1-(M-this.o)/(this.i-this.o)-.5),0),position:"absolute",left:0,top:0,pointerEvents:"none",WebkitTransition:x?null:"opacity 0.25s",MozTransition:x?null:"opacity 0.25s",transition:x?null:"opacity 0.25s"},C={height:this.t,width:this.t,opacity:Math.max(2*((M-this.o)/(this.i-this.o)-.5),0),position:"absolute",left:0,top:0,pointerEvents:"none",WebkitTransition:x?null:"opacity 0.25s",MozTransition:x?null:"opacity 0.25s",transition:x?null:"opacity 0.25s"};return i.createElement("div",{className:s,style:D},i.createElement("div",{className:"react-switch-bg",style:S,onClick:n?null:this.T,onMouseDown:function(t){return t.preventDefault()}},c&&i.createElement("div",{style:E},c),u&&i.createElement("div",{style:O},u)),i.createElement("div",{className:"react-switch-handle",style:A,onClick:function(t){return t.preventDefault()},onMouseDown:n?null:this.p,onTouchStart:n?null:this.k,onTouchMove:n?null:this.M,onTouchEnd:n?null:this.m,onTouchCancel:n?null:this.O},d&&i.createElement("div",{style:T},d),g&&i.createElement("div",{style:C},g)),i.createElement("input",r({},{type:"checkbox",role:"switch","aria-checked":e,checked:e,disabled:n,style:{border:0,clip:"rect(0 0 0 0)",height:1,margin:-1,overflow:"hidden",padding:0,position:"absolute",width:1}},w,{ref:this.S,onFocus:this.D,onBlur:this.O,onKeyUp:this.C,onChange:this.$})))},e}(i.Component);f.defaultProps={disabled:!1,offColor:"#888",onColor:"#080",offHandleColor:"#fff",onHandleColor:"#fff",uncheckedIcon:s,checkedIcon:o,boxShadow:null,activeBoxShadow:"0 0 2px 3px #3bf",height:28,width:56},e.default=f},99755:function(t,e,n){t.exports=n(19313)},10523:function(t,e,n){"use strict";n.d(e,{qY:function(){return g}});var i=n(73173),r=function(t,e,n){if(n||2===arguments.length)for(var i,r=0,s=e.length;r<s;r++)!i&&r in e||(i||(i=Array.prototype.slice.call(e,0,r)),i[r]=e[r]);return t.concat(i||Array.prototype.slice.call(e))},s=function(t,e,n){this.name=t,this.version=e,this.os=n,this.type="browser"},o=function(t){this.version=t,this.type="node",this.name="node",this.os=i.platform},h=function(t,e,n,i){this.name=t,this.version=e,this.os=n,this.bot=i,this.type="bot-device"},a=function(){this.type="bot",this.bot=!0,this.name="bot",this.version=null,this.os=null},f=function(){this.type="react-native",this.name="react-native",this.version=null,this.os=null},l=/(nuhk|curl|Googlebot|Yammybot|Openbot|Slurp|MSNBot|Ask\ Jeeves\/Teoma|ia_archiver)/,c=[["aol",/AOLShield\/([0-9\._]+)/],["edge",/Edge\/([0-9\._]+)/],["edge-ios",/EdgiOS\/([0-9\._]+)/],["yandexbrowser",/YaBrowser\/([0-9\._]+)/],["kakaotalk",/KAKAOTALK\s([0-9\.]+)/],["samsung",/SamsungBrowser\/([0-9\.]+)/],["silk",/\bSilk\/([0-9._-]+)\b/],["miui",/MiuiBrowser\/([0-9\.]+)$/],["beaker",/BeakerBrowser\/([0-9\.]+)/],["edge-chromium",/EdgA?\/([0-9\.]+)/],["chromium-webview",/(?!Chrom.*OPR)wv\).*Chrom(?:e|ium)\/([0-9\.]+)(:?\s|$)/],["chrome",/(?!Chrom.*OPR)Chrom(?:e|ium)\/([0-9\.]+)(:?\s|$)/],["phantomjs",/PhantomJS\/([0-9\.]+)(:?\s|$)/],["crios",/CriOS\/([0-9\.]+)(:?\s|$)/],["firefox",/Firefox\/([0-9\.]+)(?:\s|$)/],["fxios",/FxiOS\/([0-9\.]+)/],["opera-mini",/Opera Mini.*Version\/([0-9\.]+)/],["opera",/Opera\/([0-9\.]+)(?:\s|$)/],["opera",/OPR\/([0-9\.]+)(:?\s|$)/],["pie",/^Microsoft Pocket Internet Explorer\/(\d+\.\d+)$/],["pie",/^Mozilla\/\d\.\d+\s\(compatible;\s(?:MSP?IE|MSInternet Explorer) (\d+\.\d+);.*Windows CE.*\)$/],["netfront",/^Mozilla\/\d\.\d+.*NetFront\/(\d.\d)/],["ie",/Trident\/7\.0.*rv\:([0-9\.]+).*\).*Gecko$/],["ie",/MSIE\s([0-9\.]+);.*Trident\/[4-7].0/],["ie",/MSIE\s(7\.0)/],["bb10",/BB10;\sTouch.*Version\/([0-9\.]+)/],["android",/Android\s([0-9\.]+)/],["ios",/Version\/([0-9\._]+).*Mobile.*Safari.*/],["safari",/Version\/([0-9\._]+).*Safari/],["facebook",/FB[AS]V\/([0-9\.]+)/],["instagram",/Instagram\s([0-9\.]+)/],["ios-webview",/AppleWebKit\/([0-9\.]+).*Mobile/],["ios-webview",/AppleWebKit\/([0-9\.]+).*Gecko\)$/],["curl",/^curl\/([0-9\.]+)$/],["searchbot",/alexa|bot|crawl(er|ing)|facebookexternalhit|feedburner|google web preview|nagios|postrank|pingdom|slurp|spider|yahoo!|yandex/]],u=[["iOS",/iP(hone|od|ad)/],["Android OS",/Android/],["BlackBerry OS",/BlackBerry|BB10/],["Windows Mobile",/IEMobile/],["Amazon OS",/Kindle/],["Windows 3.11",/Win16/],["Windows 95",/(Windows 95)|(Win95)|(Windows_95)/],["Windows 98",/(Windows 98)|(Win98)/],["Windows 2000",/(Windows NT 5.0)|(Windows 2000)/],["Windows XP",/(Windows NT 5.1)|(Windows XP)/],["Windows Server 2003",/(Windows NT 5.2)/],["Windows Vista",/(Windows NT 6.0)/],["Windows 7",/(Windows NT 6.1)/],["Windows 8",/(Windows NT 6.2)/],["Windows 8.1",/(Windows NT 6.3)/],["Windows 10",/(Windows NT 10.0)/],["Windows ME",/Windows ME/],["Windows CE",/Windows CE|WinCE|Microsoft Pocket Internet Explorer/],["Open BSD",/OpenBSD/],["Sun OS",/SunOS/],["Chrome OS",/CrOS/],["Linux",/(Linux)|(X11)/],["Mac OS",/(Mac_PowerPC)|(Macintosh)/],["QNX",/QNX/],["BeOS",/BeOS/],["OS/2",/OS\/2/]];function g(t){return t?p(t):"undefined"===typeof document&&"undefined"!==typeof navigator&&"ReactNative"===navigator.product?new f:"undefined"!==typeof navigator?p(navigator.userAgent):"undefined"!==typeof i&&i.version?new o(i.version.slice(1)):null}function d(t){return""!==t&&c.reduce((function(e,n){var i=n[0],r=n[1];if(e)return e;var s=r.exec(t);return!!s&&[i,s]}),!1)}function p(t){var e=d(t);if(!e)return null;var n=e[0],i=e[1];if("searchbot"===n)return new a;var o=i[1]&&i[1].split(".").join("_").split("_").slice(0,3);o?o.length<3&&(o=r(r([],o,!0),function(t){for(var e=[],n=0;n<t;n++)e.push("0");return e}(3-o.length),!0)):o=[];var f=o.join("."),c=function(t){for(var e=0,n=u.length;e<n;e++){var i=u[e],r=i[0];if(i[1].exec(t))return r}return null}(t),g=l.exec(t);return g&&g[1]?new h(n,f,c,g[1]):new s(n,f,c)}},99667:function(t){var e=function(){this.Diff_Timeout=1,this.Diff_EditCost=4,this.Match_Threshold=.5,this.Match_Distance=1e3,this.Patch_DeleteThreshold=.5,this.Patch_Margin=4,this.Match_MaxBits=32},n=-1;e.Diff=function(t,e){return[t,e]},e.prototype.diff_main=function(t,n,i,r){"undefined"==typeof r&&(r=this.Diff_Timeout<=0?Number.MAX_VALUE:(new Date).getTime()+1e3*this.Diff_Timeout);var s=r;if(null==t||null==n)throw new Error("Null input. (diff_main)");if(t==n)return t?[new e.Diff(0,t)]:[];"undefined"==typeof i&&(i=!0);var o=i,h=this.diff_commonPrefix(t,n),a=t.substring(0,h);t=t.substring(h),n=n.substring(h),h=this.diff_commonSuffix(t,n);var f=t.substring(t.length-h);t=t.substring(0,t.length-h),n=n.substring(0,n.length-h);var l=this.diff_compute_(t,n,o,s);return a&&l.unshift(new e.Diff(0,a)),f&&l.push(new e.Diff(0,f)),this.diff_cleanupMerge(l),l},e.prototype.diff_compute_=function(t,i,r,s){var o;if(!t)return[new e.Diff(1,i)];if(!i)return[new e.Diff(n,t)];var h=t.length>i.length?t:i,a=t.length>i.length?i:t,f=h.indexOf(a);if(-1!=f)return o=[new e.Diff(1,h.substring(0,f)),new e.Diff(0,a),new e.Diff(1,h.substring(f+a.length))],t.length>i.length&&(o[0][0]=o[2][0]=n),o;if(1==a.length)return[new e.Diff(n,t),new e.Diff(1,i)];var l=this.diff_halfMatch_(t,i);if(l){var c=l[0],u=l[1],g=l[2],d=l[3],p=l[4],b=this.diff_main(c,g,r,s),v=this.diff_main(u,d,r,s);return b.concat([new e.Diff(0,p)],v)}return r&&t.length>100&&i.length>100?this.diff_lineMode_(t,i,s):this.diff_bisect_(t,i,s)},e.prototype.diff_lineMode_=function(t,i,r){var s=this.diff_linesToChars_(t,i);t=s.chars1,i=s.chars2;var o=s.lineArray,h=this.diff_main(t,i,!1,r);this.diff_charsToLines_(h,o),this.diff_cleanupSemantic(h),h.push(new e.Diff(0,""));for(var a=0,f=0,l=0,c="",u="";a<h.length;){switch(h[a][0]){case 1:l++,u+=h[a][1];break;case n:f++,c+=h[a][1];break;case 0:if(f>=1&&l>=1){h.splice(a-f-l,f+l),a=a-f-l;for(var g=this.diff_main(c,u,!1,r),d=g.length-1;d>=0;d--)h.splice(a,0,g[d]);a+=g.length}l=0,f=0,c="",u=""}a++}return h.pop(),h},e.prototype.diff_bisect_=function(t,i,r){for(var s=t.length,o=i.length,h=Math.ceil((s+o)/2),a=h,f=2*h,l=new Array(f),c=new Array(f),u=0;u<f;u++)l[u]=-1,c[u]=-1;l[a+1]=0,c[a+1]=0;for(var g=s-o,d=g%2!=0,p=0,b=0,v=0,_=0,m=0;m<h&&!((new Date).getTime()>r);m++){for(var w=-m+p;w<=m-b;w+=2){for(var y=a+w,M=(E=w==-m||w!=m&&l[y-1]<l[y+1]?l[y+1]:l[y-1]+1)-w;E<s&&M<o&&t.charAt(E)==i.charAt(M);)E++,M++;if(l[y]=E,E>s)b+=2;else if(M>o)p+=2;else if(d){if((D=a+g-w)>=0&&D<f&&-1!=c[D])if(E>=(k=s-c[D]))return this.diff_bisectSplit_(t,i,E,M,r)}}for(var x=-m+v;x<=m-_;x+=2){for(var k,D=a+x,S=(k=x==-m||x!=m&&c[D-1]<c[D+1]?c[D+1]:c[D-1]+1)-x;k<s&&S<o&&t.charAt(s-k-1)==i.charAt(o-S-1);)k++,S++;if(c[D]=k,k>s)_+=2;else if(S>o)v+=2;else if(!d){if((y=a+g-x)>=0&&y<f&&-1!=l[y]){var E;M=a+(E=l[y])-y;if(E>=(k=s-k))return this.diff_bisectSplit_(t,i,E,M,r)}}}}return[new e.Diff(n,t),new e.Diff(1,i)]},e.prototype.diff_bisectSplit_=function(t,e,n,i,r){var s=t.substring(0,n),o=e.substring(0,i),h=t.substring(n),a=e.substring(i),f=this.diff_main(s,o,!1,r),l=this.diff_main(h,a,!1,r);return f.concat(l)},e.prototype.diff_linesToChars_=function(t,e){var n=[],i={};function r(t){for(var e="",r=0,o=-1,h=n.length;o<t.length-1;){-1==(o=t.indexOf("\n",r))&&(o=t.length-1);var a=t.substring(r,o+1);(i.hasOwnProperty?i.hasOwnProperty(a):void 0!==i[a])?e+=String.fromCharCode(i[a]):(h==s&&(a=t.substring(r),o=t.length),e+=String.fromCharCode(h),i[a]=h,n[h++]=a),r=o+1}return e}n[0]="";var s=4e4,o=r(t);return s=65535,{chars1:o,chars2:r(e),lineArray:n}},e.prototype.diff_charsToLines_=function(t,e){for(var n=0;n<t.length;n++){for(var i=t[n][1],r=[],s=0;s<i.length;s++)r[s]=e[i.charCodeAt(s)];t[n][1]=r.join("")}},e.prototype.diff_commonPrefix=function(t,e){if(!t||!e||t.charAt(0)!=e.charAt(0))return 0;for(var n=0,i=Math.min(t.length,e.length),r=i,s=0;n<r;)t.substring(s,r)==e.substring(s,r)?s=n=r:i=r,r=Math.floor((i-n)/2+n);return r},e.prototype.diff_commonSuffix=function(t,e){if(!t||!e||t.charAt(t.length-1)!=e.charAt(e.length-1))return 0;for(var n=0,i=Math.min(t.length,e.length),r=i,s=0;n<r;)t.substring(t.length-r,t.length-s)==e.substring(e.length-r,e.length-s)?s=n=r:i=r,r=Math.floor((i-n)/2+n);return r},e.prototype.diff_commonOverlap_=function(t,e){var n=t.length,i=e.length;if(0==n||0==i)return 0;n>i?t=t.substring(n-i):n<i&&(e=e.substring(0,n));var r=Math.min(n,i);if(t==e)return r;for(var s=0,o=1;;){var h=t.substring(r-o),a=e.indexOf(h);if(-1==a)return s;o+=a,0!=a&&t.substring(r-o)!=e.substring(0,o)||(s=o,o++)}},e.prototype.diff_halfMatch_=function(t,e){if(this.Diff_Timeout<=0)return null;var n=t.length>e.length?t:e,i=t.length>e.length?e:t;if(n.length<4||2*i.length<n.length)return null;var r=this;function s(t,e,n){for(var i,s,o,h,a=t.substring(n,n+Math.floor(t.length/4)),f=-1,l="";-1!=(f=e.indexOf(a,f+1));){var c=r.diff_commonPrefix(t.substring(n),e.substring(f)),u=r.diff_commonSuffix(t.substring(0,n),e.substring(0,f));l.length<u+c&&(l=e.substring(f-u,f)+e.substring(f,f+c),i=t.substring(0,n-u),s=t.substring(n+c),o=e.substring(0,f-u),h=e.substring(f+c))}return 2*l.length>=t.length?[i,s,o,h,l]:null}var o,h,a,f,l,c=s(n,i,Math.ceil(n.length/4)),u=s(n,i,Math.ceil(n.length/2));return c||u?(o=u?c&&c[4].length>u[4].length?c:u:c,t.length>e.length?(h=o[0],a=o[1],f=o[2],l=o[3]):(f=o[0],l=o[1],h=o[2],a=o[3]),[h,a,f,l,o[4]]):null},e.prototype.diff_cleanupSemantic=function(t){for(var i=!1,r=[],s=0,o=null,h=0,a=0,f=0,l=0,c=0;h<t.length;)0==t[h][0]?(r[s++]=h,a=l,f=c,l=0,c=0,o=t[h][1]):(1==t[h][0]?l+=t[h][1].length:c+=t[h][1].length,o&&o.length<=Math.max(a,f)&&o.length<=Math.max(l,c)&&(t.splice(r[s-1],0,new e.Diff(n,o)),t[r[s-1]+1][0]=1,s--,h=--s>0?r[s-1]:-1,a=0,f=0,l=0,c=0,o=null,i=!0)),h++;for(i&&this.diff_cleanupMerge(t),this.diff_cleanupSemanticLossless(t),h=1;h<t.length;){if(t[h-1][0]==n&&1==t[h][0]){var u=t[h-1][1],g=t[h][1],d=this.diff_commonOverlap_(u,g),p=this.diff_commonOverlap_(g,u);d>=p?(d>=u.length/2||d>=g.length/2)&&(t.splice(h,0,new e.Diff(0,g.substring(0,d))),t[h-1][1]=u.substring(0,u.length-d),t[h+1][1]=g.substring(d),h++):(p>=u.length/2||p>=g.length/2)&&(t.splice(h,0,new e.Diff(0,u.substring(0,p))),t[h-1][0]=1,t[h-1][1]=g.substring(0,g.length-p),t[h+1][0]=n,t[h+1][1]=u.substring(p),h++),h++}h++}},e.prototype.diff_cleanupSemanticLossless=function(t){function n(t,n){if(!t||!n)return 6;var i=t.charAt(t.length-1),r=n.charAt(0),s=i.match(e.nonAlphaNumericRegex_),o=r.match(e.nonAlphaNumericRegex_),h=s&&i.match(e.whitespaceRegex_),a=o&&r.match(e.whitespaceRegex_),f=h&&i.match(e.linebreakRegex_),l=a&&r.match(e.linebreakRegex_),c=f&&t.match(e.blanklineEndRegex_),u=l&&n.match(e.blanklineStartRegex_);return c||u?5:f||l?4:s&&!h&&a?3:h||a?2:s||o?1:0}for(var i=1;i<t.length-1;){if(0==t[i-1][0]&&0==t[i+1][0]){var r=t[i-1][1],s=t[i][1],o=t[i+1][1],h=this.diff_commonSuffix(r,s);if(h){var a=s.substring(s.length-h);r=r.substring(0,r.length-h),s=a+s.substring(0,s.length-h),o=a+o}for(var f=r,l=s,c=o,u=n(r,s)+n(s,o);s.charAt(0)===o.charAt(0);){r+=s.charAt(0),s=s.substring(1)+o.charAt(0),o=o.substring(1);var g=n(r,s)+n(s,o);g>=u&&(u=g,f=r,l=s,c=o)}t[i-1][1]!=f&&(f?t[i-1][1]=f:(t.splice(i-1,1),i--),t[i][1]=l,c?t[i+1][1]=c:(t.splice(i+1,1),i--))}i++}},e.nonAlphaNumericRegex_=/[^a-zA-Z0-9]/,e.whitespaceRegex_=/\s/,e.linebreakRegex_=/[\r\n]/,e.blanklineEndRegex_=/\n\r?\n$/,e.blanklineStartRegex_=/^\r?\n\r?\n/,e.prototype.diff_cleanupEfficiency=function(t){for(var i=!1,r=[],s=0,o=null,h=0,a=!1,f=!1,l=!1,c=!1;h<t.length;)0==t[h][0]?(t[h][1].length<this.Diff_EditCost&&(l||c)?(r[s++]=h,a=l,f=c,o=t[h][1]):(s=0,o=null),l=c=!1):(t[h][0]==n?c=!0:l=!0,o&&(a&&f&&l&&c||o.length<this.Diff_EditCost/2&&a+f+l+c==3)&&(t.splice(r[s-1],0,new e.Diff(n,o)),t[r[s-1]+1][0]=1,s--,o=null,a&&f?(l=c=!0,s=0):(h=--s>0?r[s-1]:-1,l=c=!1),i=!0)),h++;i&&this.diff_cleanupMerge(t)},e.prototype.diff_cleanupMerge=function(t){t.push(new e.Diff(0,""));for(var i,r=0,s=0,o=0,h="",a="";r<t.length;)switch(t[r][0]){case 1:o++,a+=t[r][1],r++;break;case n:s++,h+=t[r][1],r++;break;case 0:s+o>1?(0!==s&&0!==o&&(0!==(i=this.diff_commonPrefix(a,h))&&(r-s-o>0&&0==t[r-s-o-1][0]?t[r-s-o-1][1]+=a.substring(0,i):(t.splice(0,0,new e.Diff(0,a.substring(0,i))),r++),a=a.substring(i),h=h.substring(i)),0!==(i=this.diff_commonSuffix(a,h))&&(t[r][1]=a.substring(a.length-i)+t[r][1],a=a.substring(0,a.length-i),h=h.substring(0,h.length-i))),r-=s+o,t.splice(r,s+o),h.length&&(t.splice(r,0,new e.Diff(n,h)),r++),a.length&&(t.splice(r,0,new e.Diff(1,a)),r++),r++):0!==r&&0==t[r-1][0]?(t[r-1][1]+=t[r][1],t.splice(r,1)):r++,o=0,s=0,h="",a=""}""===t[t.length-1][1]&&t.pop();var f=!1;for(r=1;r<t.length-1;)0==t[r-1][0]&&0==t[r+1][0]&&(t[r][1].substring(t[r][1].length-t[r-1][1].length)==t[r-1][1]?(t[r][1]=t[r-1][1]+t[r][1].substring(0,t[r][1].length-t[r-1][1].length),t[r+1][1]=t[r-1][1]+t[r+1][1],t.splice(r-1,1),f=!0):t[r][1].substring(0,t[r+1][1].length)==t[r+1][1]&&(t[r-1][1]+=t[r+1][1],t[r][1]=t[r][1].substring(t[r+1][1].length)+t[r+1][1],t.splice(r+1,1),f=!0)),r++;f&&this.diff_cleanupMerge(t)},e.prototype.diff_xIndex=function(t,e){var i,r=0,s=0,o=0,h=0;for(i=0;i<t.length&&(1!==t[i][0]&&(r+=t[i][1].length),t[i][0]!==n&&(s+=t[i][1].length),!(r>e));i++)o=r,h=s;return t.length!=i&&t[i][0]===n?h:h+(e-o)},e.prototype.diff_prettyHtml=function(t){for(var e=[],i=/&/g,r=/</g,s=/>/g,o=/\n/g,h=0;h<t.length;h++){var a=t[h][0],f=t[h][1].replace(i,"&amp;").replace(r,"&lt;").replace(s,"&gt;").replace(o,"&para;<br>");switch(a){case 1:e[h]='<ins style="background:#e6ffe6;">'+f+"</ins>";break;case n:e[h]='<del style="background:#ffe6e6;">'+f+"</del>";break;case 0:e[h]="<span>"+f+"</span>"}}return e.join("")},e.prototype.diff_text1=function(t){for(var e=[],n=0;n<t.length;n++)1!==t[n][0]&&(e[n]=t[n][1]);return e.join("")},e.prototype.diff_text2=function(t){for(var e=[],i=0;i<t.length;i++)t[i][0]!==n&&(e[i]=t[i][1]);return e.join("")},e.prototype.diff_levenshtein=function(t){for(var e=0,i=0,r=0,s=0;s<t.length;s++){var o=t[s][0],h=t[s][1];switch(o){case 1:i+=h.length;break;case n:r+=h.length;break;case 0:e+=Math.max(i,r),i=0,r=0}}return e+=Math.max(i,r)},e.prototype.diff_toDelta=function(t){for(var e=[],i=0;i<t.length;i++)switch(t[i][0]){case 1:e[i]="+"+encodeURI(t[i][1]);break;case n:e[i]="-"+t[i][1].length;break;case 0:e[i]="="+t[i][1].length}return e.join("\t").replace(/%20/g," ")},e.prototype.diff_fromDelta=function(t,i){for(var r=[],s=0,o=0,h=i.split(/\t/g),a=0;a<h.length;a++){var f=h[a].substring(1);switch(h[a].charAt(0)){case"+":try{r[s++]=new e.Diff(1,decodeURI(f))}catch(u){throw new Error("Illegal escape in diff_fromDelta: "+f)}break;case"-":case"=":var l=parseInt(f,10);if(isNaN(l)||l<0)throw new Error("Invalid number in diff_fromDelta: "+f);var c=t.substring(o,o+=l);"="==h[a].charAt(0)?r[s++]=new e.Diff(0,c):r[s++]=new e.Diff(n,c);break;default:if(h[a])throw new Error("Invalid diff operation in diff_fromDelta: "+h[a])}}if(o!=t.length)throw new Error("Delta length ("+o+") does not equal source text length ("+t.length+").");return r},e.prototype.match_main=function(t,e,n){if(null==t||null==e||null==n)throw new Error("Null input. (match_main)");return n=Math.max(0,Math.min(n,t.length)),t==e?0:t.length?t.substring(n,n+e.length)==e?n:this.match_bitap_(t,e,n):-1},e.prototype.match_bitap_=function(t,e,n){if(e.length>this.Match_MaxBits)throw new Error("Pattern too long for this browser.");var i=this.match_alphabet_(e),r=this;function s(t,i){var s=t/e.length,o=Math.abs(n-i);return r.Match_Distance?s+o/r.Match_Distance:o?1:s}var o=this.Match_Threshold,h=t.indexOf(e,n);-1!=h&&(o=Math.min(s(0,h),o),-1!=(h=t.lastIndexOf(e,n+e.length))&&(o=Math.min(s(0,h),o)));var a,f,l=1<<e.length-1;h=-1;for(var c,u=e.length+t.length,g=0;g<e.length;g++){for(a=0,f=u;a<f;)s(g,n+f)<=o?a=f:u=f,f=Math.floor((u-a)/2+a);u=f;var d=Math.max(1,n-f+1),p=Math.min(n+f,t.length)+e.length,b=Array(p+2);b[p+1]=(1<<g)-1;for(var v=p;v>=d;v--){var _=i[t.charAt(v-1)];if(b[v]=0===g?(b[v+1]<<1|1)&_:(b[v+1]<<1|1)&_|(c[v+1]|c[v])<<1|1|c[v+1],b[v]&l){var m=s(g,v-1);if(m<=o){if(o=m,!((h=v-1)>n))break;d=Math.max(1,2*n-h)}}}if(s(g+1,n)>o)break;c=b}return h},e.prototype.match_alphabet_=function(t){for(var e={},n=0;n<t.length;n++)e[t.charAt(n)]=0;for(n=0;n<t.length;n++)e[t.charAt(n)]|=1<<t.length-n-1;return e},e.prototype.patch_addContext_=function(t,n){if(0!=n.length){if(null===t.start2)throw Error("patch not initialized");for(var i=n.substring(t.start2,t.start2+t.length1),r=0;n.indexOf(i)!=n.lastIndexOf(i)&&i.length<this.Match_MaxBits-this.Patch_Margin-this.Patch_Margin;)r+=this.Patch_Margin,i=n.substring(t.start2-r,t.start2+t.length1+r);r+=this.Patch_Margin;var s=n.substring(t.start2-r,t.start2);s&&t.diffs.unshift(new e.Diff(0,s));var o=n.substring(t.start2+t.length1,t.start2+t.length1+r);o&&t.diffs.push(new e.Diff(0,o)),t.start1-=s.length,t.start2-=s.length,t.length1+=s.length+o.length,t.length2+=s.length+o.length}},e.prototype.patch_make=function(t,i,r){var s,o;if("string"==typeof t&&"string"==typeof i&&"undefined"==typeof r)s=t,(o=this.diff_main(s,i,!0)).length>2&&(this.diff_cleanupSemantic(o),this.diff_cleanupEfficiency(o));else if(t&&"object"==typeof t&&"undefined"==typeof i&&"undefined"==typeof r)o=t,s=this.diff_text1(o);else if("string"==typeof t&&i&&"object"==typeof i&&"undefined"==typeof r)s=t,o=i;else{if("string"!=typeof t||"string"!=typeof i||!r||"object"!=typeof r)throw new Error("Unknown call format to patch_make.");s=t,o=r}if(0===o.length)return[];for(var h=[],a=new e.patch_obj,f=0,l=0,c=0,u=s,g=s,d=0;d<o.length;d++){var p=o[d][0],b=o[d][1];switch(f||0===p||(a.start1=l,a.start2=c),p){case 1:a.diffs[f++]=o[d],a.length2+=b.length,g=g.substring(0,c)+b+g.substring(c);break;case n:a.length1+=b.length,a.diffs[f++]=o[d],g=g.substring(0,c)+g.substring(c+b.length);break;case 0:b.length<=2*this.Patch_Margin&&f&&o.length!=d+1?(a.diffs[f++]=o[d],a.length1+=b.length,a.length2+=b.length):b.length>=2*this.Patch_Margin&&f&&(this.patch_addContext_(a,u),h.push(a),a=new e.patch_obj,f=0,u=g,l=c)}1!==p&&(l+=b.length),p!==n&&(c+=b.length)}return f&&(this.patch_addContext_(a,u),h.push(a)),h},e.prototype.patch_deepCopy=function(t){for(var n=[],i=0;i<t.length;i++){var r=t[i],s=new e.patch_obj;s.diffs=[];for(var o=0;o<r.diffs.length;o++)s.diffs[o]=new e.Diff(r.diffs[o][0],r.diffs[o][1]);s.start1=r.start1,s.start2=r.start2,s.length1=r.length1,s.length2=r.length2,n[i]=s}return n},e.prototype.patch_apply=function(t,e){if(0==t.length)return[e,[]];t=this.patch_deepCopy(t);var i=this.patch_addPadding(t);e=i+e+i,this.patch_splitMax(t);for(var r=0,s=[],o=0;o<t.length;o++){var h,a,f=t[o].start2+r,l=this.diff_text1(t[o].diffs),c=-1;if(l.length>this.Match_MaxBits?-1!=(h=this.match_main(e,l.substring(0,this.Match_MaxBits),f))&&(-1==(c=this.match_main(e,l.substring(l.length-this.Match_MaxBits),f+l.length-this.Match_MaxBits))||h>=c)&&(h=-1):h=this.match_main(e,l,f),-1==h)s[o]=!1,r-=t[o].length2-t[o].length1;else if(s[o]=!0,r=h-f,l==(a=-1==c?e.substring(h,h+l.length):e.substring(h,c+this.Match_MaxBits)))e=e.substring(0,h)+this.diff_text2(t[o].diffs)+e.substring(h+l.length);else{var u=this.diff_main(l,a,!1);if(l.length>this.Match_MaxBits&&this.diff_levenshtein(u)/l.length>this.Patch_DeleteThreshold)s[o]=!1;else{this.diff_cleanupSemanticLossless(u);for(var g,d=0,p=0;p<t[o].diffs.length;p++){var b=t[o].diffs[p];0!==b[0]&&(g=this.diff_xIndex(u,d)),1===b[0]?e=e.substring(0,h+g)+b[1]+e.substring(h+g):b[0]===n&&(e=e.substring(0,h+g)+e.substring(h+this.diff_xIndex(u,d+b[1].length))),b[0]!==n&&(d+=b[1].length)}}}}return[e=e.substring(i.length,e.length-i.length),s]},e.prototype.patch_addPadding=function(t){for(var n=this.Patch_Margin,i="",r=1;r<=n;r++)i+=String.fromCharCode(r);for(r=0;r<t.length;r++)t[r].start1+=n,t[r].start2+=n;var s=t[0],o=s.diffs;if(0==o.length||0!=o[0][0])o.unshift(new e.Diff(0,i)),s.start1-=n,s.start2-=n,s.length1+=n,s.length2+=n;else if(n>o[0][1].length){var h=n-o[0][1].length;o[0][1]=i.substring(o[0][1].length)+o[0][1],s.start1-=h,s.start2-=h,s.length1+=h,s.length2+=h}if(0==(o=(s=t[t.length-1]).diffs).length||0!=o[o.length-1][0])o.push(new e.Diff(0,i)),s.length1+=n,s.length2+=n;else if(n>o[o.length-1][1].length){h=n-o[o.length-1][1].length;o[o.length-1][1]+=i.substring(0,h),s.length1+=h,s.length2+=h}return i},e.prototype.patch_splitMax=function(t){for(var i=this.Match_MaxBits,r=0;r<t.length;r++)if(!(t[r].length1<=i)){var s=t[r];t.splice(r--,1);for(var o=s.start1,h=s.start2,a="";0!==s.diffs.length;){var f=new e.patch_obj,l=!0;for(f.start1=o-a.length,f.start2=h-a.length,""!==a&&(f.length1=f.length2=a.length,f.diffs.push(new e.Diff(0,a)));0!==s.diffs.length&&f.length1<i-this.Patch_Margin;){var c=s.diffs[0][0],u=s.diffs[0][1];1===c?(f.length2+=u.length,h+=u.length,f.diffs.push(s.diffs.shift()),l=!1):c===n&&1==f.diffs.length&&0==f.diffs[0][0]&&u.length>2*i?(f.length1+=u.length,o+=u.length,l=!1,f.diffs.push(new e.Diff(c,u)),s.diffs.shift()):(u=u.substring(0,i-f.length1-this.Patch_Margin),f.length1+=u.length,o+=u.length,0===c?(f.length2+=u.length,h+=u.length):l=!1,f.diffs.push(new e.Diff(c,u)),u==s.diffs[0][1]?s.diffs.shift():s.diffs[0][1]=s.diffs[0][1].substring(u.length))}a=(a=this.diff_text2(f.diffs)).substring(a.length-this.Patch_Margin);var g=this.diff_text1(s.diffs).substring(0,this.Patch_Margin);""!==g&&(f.length1+=g.length,f.length2+=g.length,0!==f.diffs.length&&0===f.diffs[f.diffs.length-1][0]?f.diffs[f.diffs.length-1][1]+=g:f.diffs.push(new e.Diff(0,g))),l||t.splice(++r,0,f)}}},e.prototype.patch_toText=function(t){for(var e=[],n=0;n<t.length;n++)e[n]=t[n];return e.join("")},e.prototype.patch_fromText=function(t){var i=[];if(!t)return i;for(var r=t.split("\n"),s=0,o=/^@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@$/;s<r.length;){var h=r[s].match(o);if(!h)throw new Error("Invalid patch string: "+r[s]);var a=new e.patch_obj;for(i.push(a),a.start1=parseInt(h[1],10),""===h[2]?(a.start1--,a.length1=1):"0"==h[2]?a.length1=0:(a.start1--,a.length1=parseInt(h[2],10)),a.start2=parseInt(h[3],10),""===h[4]?(a.start2--,a.length2=1):"0"==h[4]?a.length2=0:(a.start2--,a.length2=parseInt(h[4],10)),s++;s<r.length;){var f=r[s].charAt(0);try{var l=decodeURI(r[s].substring(1))}catch(c){throw new Error("Illegal escape in patch_fromText: "+l)}if("-"==f)a.diffs.push(new e.Diff(n,l));else if("+"==f)a.diffs.push(new e.Diff(1,l));else if(" "==f)a.diffs.push(new e.Diff(0,l));else{if("@"==f)break;if(""!==f)throw new Error('Invalid patch mode "'+f+'" in: '+l)}s++}}return i},(e.patch_obj=function(){this.diffs=[],this.start1=null,this.start2=null,this.length1=0,this.length2=0}).prototype.toString=function(){for(var t,e=["@@ -"+(0===this.length1?this.start1+",0":1==this.length1?this.start1+1:this.start1+1+","+this.length1)+" +"+(0===this.length2?this.start2+",0":1==this.length2?this.start2+1:this.start2+1+","+this.length2)+" @@\n"],i=0;i<this.diffs.length;i++){switch(this.diffs[i][0]){case 1:t="+";break;case n:t="-";break;case 0:t=" "}e[i+1]=t+encodeURI(this.diffs[i][1])+"\n"}return e.join("").replace(/%20/g," ")},t.exports=e,t.exports.diff_match_patch=e,t.exports.DIFF_DELETE=n,t.exports.DIFF_INSERT=1,t.exports.DIFF_EQUAL=0},62671:function(t,e,n){"use strict";function i(){return(i=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var n=arguments[e];for(var i in n)Object.prototype.hasOwnProperty.call(n,i)&&(t[i]=n[i])}return t}).apply(this,arguments)}n.d(e,{Z:function(){return i}})},13561:function(t,e,n){"use strict";n.d(e,{Z:function(){return r}});var i=n(29799);function r(t,e,n){return(r="undefined"!==typeof Reflect&&Reflect.get?Reflect.get:function(t,e,n){var r=function(t,e){for(;!Object.prototype.hasOwnProperty.call(t,e)&&null!==(t=(0,i.Z)(t)););return t}(t,e);if(r){var s=Object.getOwnPropertyDescriptor(r,e);return s.get?s.get.call(n):s.value}})(t,e,n||t)}}}]);
//# sourceMappingURL=2015-2fe99b25374011f63fd2.js.map