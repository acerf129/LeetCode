"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[7206],{7206:function(e,t,n){n.r(t),n.d(t,{prepareToRunPageEditorAction:function(){return B},loadWidget:function(){return F},deleteSingleArticle:function(){return X},savePage:function(){return Y},publishPage:function(){return Q},saveCollectionArticle:function(){return ee},getNewsletterSubscriptions:function(){return te},addNewsletterSubscription:function(){return ne},sendClipboardSourceRequest:function(){return re}});var r=n(93586),a=n(88753),i=n.n(a),o=n(52198),c=n(80944),u=n(16962),s=n(27913),l=n(98411),d=n(12006),p=n(44124),v=n(34560),f=n(49227),h=n(97242),g=n(74013),m=n(51127),_=n(59290),x=n(10980),b=n(56651),w=n(39064),k=n(20767),y=n(84283),S=n(60136),O=n(53114),E=n(27427),C=n(95621),T=n(37636),I=n(786),A=n.n(I),R=n(31290);function P(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function U(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?P(Object(n),!0).forEach((function(t){(0,r.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):P(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var Z=function(e,t,n,r){return function(){var a=(0,o.Z)(i().mark((function a(o){var c,u;return i().wrap((function(a){for(;;)switch(a.prev=a.next){case 0:if(!(c=JSON.parse(t))){a.next=6;break}return e=A()(e,{content:{image_id:{$set:c.image_id}}}),a.next=5,(0,R.cT)(e.content.file,c.upload_url);case 5:delete e.content.file;case 6:if(!(u=JSON.parse(n))){a.next=12;break}return e=A()(e,{content:{resized:{image_id:{$set:u.image_id}}}}),a.next=11,(0,R.cT)(e.content.resized.file,u.upload_url);case 11:delete e.content.resized.file;case 12:r?(0,E.eB)(r,e.content.comp_id,(0,R.sG)(c,u)):o(s.oh.updateContentState(e.hash,(0,R.sG)(c,u)));case 13:case"end":return a.stop()}}),a)})));return function(e){return a.apply(this,arguments)}}()},L=function(e,t,n,r,a){return function(){var u=(0,o.Z)(i().mark((function u(s){return i().wrap((function(u){for(;;)switch(u.prev=u.next){case 0:return u.abrupt("return",new Promise(function(){var u=(0,o.Z)(i().mark((function o(u,l){var d,p;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:if(i.prev=0,!(0,R.iM)(r.content)){i.next=7;break}return i.next=4,(0,c.i1)({author_id:e,collection_id:t,page_id:n});case 4:i.t0=i.sent,i.next=8;break;case 7:i.t0=null;case 8:if(d=i.t0,!(0,R.rL)(r.content)){i.next=15;break}return i.next=12,(0,c.i1)({author_id:e,collection_id:t,page_id:n});case 12:i.t1=i.sent,i.next=16;break;case 15:i.t1=null;case 16:return p=i.t1,i.next=19,s(Z(r,d,p,a));case 19:u(),i.next=25;break;case 22:i.prev=22,i.t2=i.catch(0),l(i.t2);case 25:case"end":return i.stop()}}),o,null,[[0,22]])})));return function(e,t){return u.apply(this,arguments)}}()));case 1:case"end":return u.stop()}}),u)})));return function(e){return u.apply(this,arguments)}}()},N=function(e,t,n,r,a){return function(){var u=(0,o.Z)(i().mark((function u(l){return i().wrap((function(u){for(;;)switch(u.prev=u.next){case 0:return u.abrupt("return",new Promise(function(){var u=(0,o.Z)(i().mark((function o(u,d){var p,v,h,g,m,_,x,b;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:i.prev=0,p=r,v=0;case 3:if(!(v<(null===(h=r.content)||void 0===h?void 0:h.options.length))){i.next=22;break}if((x=null===(g=r.content)||void 0===g?void 0:g.options[v]).blockType!==f.$Wo.IMAGE||null!==(m=x.content)&&void 0!==m&&null!==(_=m.data)&&void 0!==_&&_.image_id){i.next=19;break}if(!t||!e){i.next=12;break}return i.next=9,(0,c.i1)({author_id:e,collection_id:t,page_id:n});case 9:i.t0=i.sent,i.next=15;break;case 12:return i.next=14,(0,c.hv)(n);case 14:i.t0=i.sent;case 15:return b=i.t0,i.next=18,(0,C.k)(p,b,a,v,c.iL,E.eB,s.oh.updateContentState,l);case 18:p=i.sent;case 19:v++,i.next=3;break;case 22:u(),i.next=28;break;case 25:i.prev=25,i.t1=i.catch(0),d(i.t1);case 28:case"end":return i.stop()}}),o,null,[[0,25]])})));return function(e,t){return u.apply(this,arguments)}}()));case 1:case"end":return u.stop()}}),u)})));return function(e){return u.apply(this,arguments)}}()},j=function(e,t,n){return function(){var r=(0,o.Z)(i().mark((function r(a){return i().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return r.abrupt("return",new Promise(function(){var r=(0,o.Z)(i().mark((function r(o,u){var s,l;return i().wrap((function(r){for(;;)switch(r.prev=r.next){case 0:if(r.prev=0,!(0,R.iM)(e.content)){r.next=7;break}return r.next=4,(0,c.hv)(t);case 4:r.t0=r.sent,r.next=8;break;case 7:r.t0=null;case 8:if(s=r.t0,!(0,R.rL)(e.content)){r.next=15;break}return r.next=12,(0,c.hv)(t);case 12:r.t1=r.sent,r.next=16;break;case 15:r.t1=null;case 16:return l=r.t1,r.next=19,a(Z(e,s,l,n));case 19:o(),r.next=25;break;case 22:r.prev=22,r.t2=r.catch(0),u(r.t2);case 25:case"end":return r.stop()}}),r,null,[[0,22]])})));return function(e,t){return r.apply(this,arguments)}}()));case 1:case"end":return r.stop()}}),r)})));return function(e){return r.apply(this,arguments)}}()},D=function(e){return e.map((function(e){return e.content.image_id}))},M=function e(t,n){var r=0,a=t.type;switch(a){case"Image":case"Chart":case"Graph":case"Matrix":case"LinkedList":case"EducativeArray":case"BinaryTree":case"NaryTree":case"Stack":case"HashTable":case"Graphviz":case"SVGEdit":case"SVG":case"Canvas":case"MxGraphWidget":case"SequenceDiagrams":case"UML":case"Mermaid":case"MarkMap":r++}"MarkdownEditor"===a&&(r+=(t.content.mdHtml.match(/img/g)||[]).length),"Columns"===a&&t.content.comps&&t.content.comps.forEach((function(t){e(t,n)})),"CanvasAnimation"===a&&(r+=t.content.canvasObjects.length),"illustrations"in n?n.illustrations+=r:n.illustrations=r},W=function(e){var t={};return e.forEach((function(e){var n=e.type;n in t?t[n]++:t[n]=1,function(e,t){var n=0,r=0,a=0,i=e.type;if("RunJS"===i){var o,c,u,s,l=null===e||void 0===e||null===(o=e.content)||void 0===o||null===(c=o.jotted)||void 0===c?void 0:c.exercise,d=null===e||void 0===e||null===(u=e.content)||void 0===u||null===(s=u.jotted)||void 0===s?void 0:s.showSolution;l||d?r++:n++}else if("WebpackBin"===i){var p,v,f;(null===e||void 0===e||null===(p=e.content)||void 0===p||null===(v=p.codeContents)||void 0===v||null===(f=v.judge)||void 0===f?void 0:f.judgeActive)?r++:n++}else if("Code"===i)e.content.runnable?n++:e.content.judge?r++:a++;else if("TabbedCode"===i)e.content.codeContents.forEach((function(e){e.runnable?n++:e.judge?r++:a++}));else if("LiveApp"===i)n++;else if("TerminalWidget"===i)n++;else if("MarkdownEditor"===i){var h=document.createElement("div");h.innerHTML=e.content.mdHtml,a+=Array.from(h.querySelectorAll("pre")).filter((function(e){return e.querySelectorAll("code").length>0})).length}"codeExerciseCount"in t?t.codeExerciseCount+=r:t.codeExerciseCount=r,"codeRunnableCount"in t?t.codeRunnableCount+=n:t.codeRunnableCount=n,"codeSnippetCount"in t?t.codeSnippetCount+=a:t.codeSnippetCount=a}(e,t),M(e,t)})),JSON.stringify(t)},q=function(e,t,n,r,a,i){return function(o){return new Promise((function(c,l){for(var d=[],p=[],v=[],f=0;f<a.length;f++){"Image"===a[f].type||"File"===a[f].type?(v.push(a[f]),((0,R.iM)(a[f].content)||(0,R.rL)(a[f].content))&&d.push(a[f])):(0,C.o)(a[f])&&p.push(a[f]);var h=(0,O.s)(a[f]);h&&d.push(h),!a[f].content||a[f].content.comp_id||i||o(s.oh.updateContentState(a[f].hash,(function(e){e.comp_id=(0,k.x0)()})))}var g=[];if(d.length>0||p.length>0){o(u.n.update({status:"WAIT",text:"Uploading Files and Images"}));for(var m=0;m<d.length;m++)n?g.push(o(L(e,n,t,d[m],i))):g.push(o(j(d[m],t,i)));for(var _=0;_<p.length;_++)g.push(o(N(e,n,t,p[_],i)));Promise.all(g).then((function(){var e=D(v);c({cover_image:r,validImageIds:e})}),(function(e){console.error(e),l(e),o(u.n.update({status:"ERROR",text:"Uploading File or Image failed. Please retry"}))}))}else{var x=D(v);c({cover_image:r,validImageIds:x})}}))}},J=function(e,t,n,r){return JSON.stringify({components:t,summary:n,cover_image_id:r.image_id,cover_image_metadata:r.metadata})},B=function(e,t,n,r,a,s,l,p){var v=arguments.length>8&&void 0!==arguments[8]?arguments[8]:"",f=arguments.length>9?arguments[9]:void 0;return function(){var h=(0,o.Z)(i().mark((function o(h){var g,m;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:if(h(u.n.show(d.ad,{status:"WAIT",text:"Starting to Save"})),!e.file||!e.updated){i.next=20;break}return h(u.n.update({status:"WAIT",text:"Uploading Files and Images"})),i.prev=3,i.next=6,(0,c.iL)(e);case 6:return g=i.sent,(m=JSON.parse(g))&&(e.updated=!1,e.file_name=m.file_name,e.image="".concat(t,"/").concat(m.image_id),e.image_id=m.image_id),i.next=11,r(e);case 11:s(n,e,a,l,p,v,f),i.next=18;break;case 14:i.prev=14,i.t0=i.catch(3),h(u.n.update({status:"ERROR",text:"Upload Image failed"})),console.error(i.t0);case 18:i.next=21;break;case 20:s(n,e,a,l,p,v,f);case 21:case"end":return i.stop()}}),o,null,[[3,14]])})));return function(e){return h.apply(this,arguments)}}()},G=function(e,t,n,r,a,i){var o=arguments.length>6&&void 0!==arguments[6]?arguments[6]:"",c=arguments.length>7?arguments[7]:void 0;return function(u,l){var d,p,v=l().widgets.selectedHash,f=c&&(null===(d=c.children[v])||void 0===d||null===(p=d.content)||void 0===p?void 0:p.comp_id);-1!==(c?c.children.findIndex((function(e){var t;return(null===(t=e.content)||void 0===t?void 0:t.comp_id)===f&&f})):l().widgets.ids.indexOf(v))?(e((function(){return u(t(n,r,a,i,!0,o,c))})),c?(0,E.YR)(c,f):u(s.oh.bumpVersion())):u(t(n,r,a,i,!0,o,c))}},F=function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1];return function(n,r){var a,i,o,c=r().author,u=null===c||void 0===c||null===(a=c.collectionArticle)||void 0===a?void 0:a.data,l=null===c||void 0===c||null===(i=c.proofread)||void 0===i||null===(o=i.data)||void 0===o?void 0:o.page,d=t?null===l||void 0===l?void 0:l.components:null===u||void 0===u?void 0:u.components,p=r().widgets.ids.indexOf(e),v=null===d||void 0===d?void 0:d[p];return n(s.oh.addOnExistingHash({data:v,hash:e}))}},H=function(e,t,n,r,a){return function(){var t=(0,o.Z)(i().mark((function t(o,s){var l,p,v,f,h,m,_,k,y,S,O,C,T,I,A,R,P,Z,L,N,j,D,M,q;return i().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return o(u.n.showOrUpdate(d.ad,{status:"WAIT",text:"Optimizing Article to save"})),m=s(),_=m.author,_.page.data,k=_.collection,y=m.pageSummary,S=m.widgets,O=(null===k||void 0===k||null===(l=k.instance)||void 0===l?void 0:l.details.is_plan)||(null===k||void 0===k||null===(p=k.instance)||void 0===p?void 0:p.details.is_parent_plan),C=a?(0,E.gK)(a):S.ids.map((function(e){return S.entities[e]})),T=n.author_id,I=n.collection_id,A=n.page_id,t.next=7,(0,g.TE)(C);case 7:if(R=t.sent,P=R.TOC,Z=I&&(null===k||void 0===k||null===(v=k.instance)||void 0===v||null===(f=v.details)||void 0===f||null===(h=f.page_titles)||void 0===h?void 0:h[A]),delete(L=U({},y)).dirty,N=J(0,C,L,e),j=W(C),D=JSON.stringify((0,x.D)(C)),o(u.n.showOrUpdate(d.ad,{status:"WAIT",text:"Saving ".concat(O?"Task":"Article")})),o(b.I.change({titleUpdated:!0})),M=e.metadata?JSON.stringify(e.metadata):"",q=L.tags?L.tags.toString():"",I){t.next=23;break}if(A){t.next=22;break}return t.abrupt("return",new Promise((function(e){return e()})));case 22:return t.abrupt("return",(0,c.Is)({pageId:A,page_title:L.title,page_summary:L.description,page_table_of_content:P,page_table_of_content_is_enabled:L.pageTocEnabled,price:L.price,is_priced:L.is_priced||"false",version:L.version,tags:q,page_content_encoding:"deflate",page_content:N,cover_image_id:e.image_id,cover_image_metadata:M,widget_stats:j,feedback_email:L.feedback_email,feedback_email_2:L.feedback_email_2,concept_list:D,eTag:r}));case 23:return t.abrupt("return",new Promise((function(t,n){(0,c.EO)({authorId:T,collectionId:I,pageId:A,page_title:Z,page_summary:L.description,page_table_of_content:P,price:L.price,is_priced:L.is_priced,version:L.version,tags:q,page_content_encoding:"deflate",page_content:N,cover_image_id:e.image_id,cover_image_metadata:M,widget_stats:j,concept_list:D,eTag:r}).then((function(e){"success"===(null===e||void 0===e?void 0:e.status)&&o(w.X5.updateArticleTags({pageId:A,tags:q})),t()})).catch((function(e){n(e)}))})));case 24:case"end":return t.stop()}}),t)})));return function(e,n){return t.apply(this,arguments)}}()},z=function(e,t,n,r,a,v,g){var _=arguments.length>7&&void 0!==arguments[7]?arguments[7]:"",x=arguments.length>8?arguments[8]:void 0;return function(){var b=(0,o.Z)(i().mark((function b(w,k){return i().wrap((function(b){for(;;)switch(b.prev=b.next){case 0:return b.abrupt("return",new Promise(function(){var b=(0,o.Z)(i().mark((function b(y,O){var C,I,A,R,P,U,Z,L,N,j,D,M,W,J,B,G,F,z,V;return i().wrap((function(b){for(;;)switch(b.prev=b.next){case 0:if(I=k(),A=I.widgets,R=I.author,P=!(null===(C=R.collection.instance.details)||void 0===C||!C.allow_custom_styling_editor_side),U=n.author_id,Z=n.collection_id,L=n.page_id,N=x?(0,E.gK)(x):A.ids.map((function(e){return A.entities[e]})),P||!(0,h.fg)(N)){b.next=6;break}return b.abrupt("return",w(u.n.update({status:"ERROR",text:"Unable to save changes due to custom styles"})));case 6:if(b.prev=6,!A.markdownDirty){b.next=30;break}return b.prev=8,b.prev=9,b.next=12,(0,h.SB)(N,!1,f.sLn.COLLECTION);case 12:w(s.oh.resetMarkdownDirtyBit()),b.next=25;break;case 15:if(b.prev=15,b.t0=b.catch(9),!("errors"in b.t0)||!("headingTree"in b.t0)){b.next=24;break}if(j=b.t0.errors,D=b.t0.headingTree,!(null!==j&&void 0!==j?j:[]).length){b.next=22;break}return w(u.n.show(d.Xw,{workType:f.sLn.COLLECTION,errors:j,comps:N,dispatch:w,fixHeadings:function(){var e=(0,o.Z)(i().mark((function e(){var t;return i().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,(0,h.dC)(N,j,D);case 2:t=e.sent,x?(0,E.hv)(x,t):(0,h.bc)(w,t);case 4:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}()})),b.abrupt("return");case 22:b.next=25;break;case 24:throw b.t0;case 25:b.next=30;break;case 27:b.prev=27,b.t1=b.catch(8),(0,S.u)(b.t1);case 30:return b.next=32,w(q(U,L,t?Z:null,e,N,x));case 32:return M=b.sent,W=M.cover_image,M.validImageIds,b.next=37,w(H(W,0,n,a||"",x));case 37:if(x&&(0,T.qP)(T.f2.SLATE_EDITOR,T.bt.EDITOR_SAVE_CONTENT),y({selAfterSave:N.length?N[0].hash:-1}),w(m.x.updateLastModified()),!_){b.next=43;break}return b.next=43,(0,c.bU)(_,{author_id:U,collection_id:Z,page_id:L,page_type:f.sLn.COLLECTION},w);case 43:b.next=49;break;case 45:b.prev=45,b.t2=b.catch(6),(0,l.rU)(b.t2,w),b.t2.status===p.Wy.AlreadyExistsException?(w(u.n.close()),w(u.n.show(d.zN,{onConfirm:function(){return w(v(e,n,r,g,!1,_,x))},cancelText:"Cancel",confirmText:"Save",title:"Conflicts",description:"The content you are editing has changed. The previous changes will be overwritten. Are you sure you want to save?"}))):(V=(null===b.t2||void 0===b.t2||null===(J=b.t2.responseJSON)||void 0===J||null===(B=J.errors)||void 0===B?void 0:B.page_title)||(null===b.t2||void 0===b.t2||null===(G=b.t2.responseJSON)||void 0===G||null===(F=G.errors)||void 0===F?void 0:F.page_summary)||(null===b.t2||void 0===b.t2||null===(z=b.t2.responseJSON)||void 0===z?void 0:z.errorText)||"Unable to Save Changes",w(u.n.update({status:"ERROR",text:V})));case 49:r&&r();case 50:case"end":return b.stop()}}),b,null,[[6,45],[8,27],[9,15]])})));return function(e,t){return b.apply(this,arguments)}}()));case 1:case"end":return b.stop()}}),b)})));return function(e,t){return b.apply(this,arguments)}}()},V=function e(t,n,r,a){var c=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],d=arguments.length>5?arguments[5]:void 0,p=arguments.length>6?arguments[6]:void 0;return function(){var h=(0,o.Z)(i().mark((function o(h,g){var m,_,x,w,k,y,S,O,E;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:return y=g(),S=y.author,O=c?null===(m=S.page.data)||void 0===m?void 0:m[v.Zq]:f.FhE,E=(null===(_=S.collection)||void 0===_||null===(x=_.instance)||void 0===x?void 0:x.details.is_plan)||(null===(w=S.collection)||void 0===w||null===(k=w.instance)||void 0===k?void 0:k.details.is_parent_plan),i.prev=3,i.next=6,h(z(t,!1,n,r,O,e,a,d,p));case 6:h(u.n.update({status:"SUCCESS",text:"".concat(E?"Task":"Article"," Saved successfully")})),h(b.I.change({dirty:!1})),h(s.oh.resetDirtyBit()),i.next=16;break;case 11:i.prev=11,i.t0=i.catch(3),console.log(i.t0),(0,l.rU)(i.t0,h),h(u.n.update({status:"ERROR",text:"Unable to Save"}));case 16:case"end":return i.stop()}}),o,null,[[3,11]])})));return function(e,t){return h.apply(this,arguments)}}()},$=function e(t,n,r,a){var s=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],d=arguments.length>5?arguments[5]:void 0,p=arguments.length>6?arguments[6]:void 0;return function(){var h=(0,o.Z)(i().mark((function o(h,g){var m,_,x,b,w,k,y,S;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:return w=g(),k=w.user.info.data,y=n.page_id,S=s?null===(m=g())||void 0===m||null===(_=m.author)||void 0===_||null===(x=_.page)||void 0===x||null===(b=x.data)||void 0===b?void 0:b[v.Zq]:f.FhE,i.next=5,h(z(t,!1,n,r,S,e,a,d,p));case 5:return h(u.n.update({status:"WAIT",text:"Publishing Article"})),i.abrupt("return",(0,c.eb)(y).then((function(){h(u.n.update({status:"SUCCESS",text:"Article is now Published"})),a.push("/page/".concat(k.user_id,"/").concat(y))})).catch((function(e){console.log(e),(0,l.rU)(e,h),h(u.n.update({status:"ERROR",text:"Unable to Publish"}))})));case 7:case"end":return i.stop()}}),o)})));return function(e,t){return h.apply(this,arguments)}}()},K=function e(t,n,r,a){var c=!(arguments.length>4&&void 0!==arguments[4])||arguments[4],d=arguments.length>5&&void 0!==arguments[5]?arguments[5]:"",p=arguments.length>6?arguments[6]:void 0;return function(){var h=(0,o.Z)(i().mark((function o(h,g){var m,_,x,w,k,y,S,O,E;return i().wrap((function(i){for(;;)switch(i.prev=i.next){case 0:return y=g(),S=y.author,O=c?null===(m=S.collectionArticle.data)||void 0===m?void 0:m[v.Zq]:f.FhE,E=(null===(_=S.collection)||void 0===_||null===(x=_.instance)||void 0===x?void 0:x.details.is_plan)||(null===(w=S.collection)||void 0===w||null===(k=w.instance)||void 0===k?void 0:k.details.is_parent_plan),i.prev=3,i.next=6,h(z(t,!0,n,r,O,e,a,d,p));case 6:h(u.n.update({status:"SUCCESS",text:"".concat(E?"Task":"Article"," Saved successfully")})),h(b.I.change({dirty:!1})),h(s.oh.resetDirtyBit()),i.next=16;break;case 11:i.prev=11,i.t0=i.catch(3),console.log(i.t0),(0,l.rU)(i.t0,h),h(u.n.update({status:"ERROR",text:"Unable to Save"}));case 16:case"end":return i.stop()}}),o,null,[[3,11]])})));return function(e,t){return h.apply(this,arguments)}}()},X=function(e,t){var n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];return function(r){return r(u.n.show(d.ad,{status:"WAIT",text:"Deleting Article"})),(0,c.CT)(e).then((function(){r(u.n.update({status:"SUCCESS",text:"Article deleted"})),r(_.B.delete(e)),n&&t.push({pathname:"/teach",query:{isDeleted:!0}})})).catch((function(e){console.log(e),(0,l.rU)(e,r),r(u.n.update({status:"ERROR",text:"Unable to Delete"}))}))}},Y=function(e,t,n,r,a,i,o){return G(e,V,t,n,r,a,i,o)},Q=function(e,t,n,r,a,i,o){return G(e,$,t,n,r,a,i,o)},ee=function(e,t,n,r,a,i,o){return G(e,K,t,n,r,a,i,o)},te=function(e){return(0,y.Z)({url:"/api/user/newsletter/".concat(e),type:"GET"})},ne=function(e,t,n){var r=void 0;return t&&n&&(r={full_name:t,email:n}),(0,y.Z)({url:"/api/user/newsletter/".concat(e),type:"POST",data:r})},re=function(e){return(0,y.Z)({url:"/api/clipboard-source-request/email",type:"POST",data:{source_request_msg:e}})}}}]);
//# sourceMappingURL=7206-b2bdb2abcd3713fd7ce9.js.map