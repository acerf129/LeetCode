"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[5825],{97837:function(e,n,t){t.d(n,{Z:function(){return O}});var r=t(20348),a=t(79003),o=t(58055),l=t(31428),i=t(27018),s=t(29799),d=t(93586),c=t(89703),u=t(30583),p=t(59087),h=t(33022),g=t(64875),f=(0,h.ZP)(g.Z).withConfig({displayName:"styles__KeyCheckbox",componentId:"d831c3-0"})(["text-align:center;margin:0px !important;"]),x=t(786),v=t.n(x),b=t(78050),m=t(12258),y=t(49227),j=t(73173);function C(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function k(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?C(Object(t),!0).forEach((function(n){(0,d.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):C(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function Z(e){var n=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}();return function(){var t,r=(0,s.Z)(e);if(n){var a=(0,s.Z)(this).constructor;t=Reflect.construct(r,arguments,a)}else t=r.apply(this,arguments);return(0,i.Z)(this,t)}}var w=function(e){(0,l.Z)(t,e);var n=Z(t);function t(){var e;(0,a.Z)(this,t);for(var l=arguments.length,i=new Array(l),s=0;s<l;s++)i[s]=arguments[s];return e=n.call.apply(n,[this].concat(i)),(0,d.Z)((0,o.Z)(e),"closeOverlay",(function(){})),(0,d.Z)((0,o.Z)(e),"handleApiKeyChange",(function(n,t,r){var a={};e.props.selectedApiKeys&&(a=k({},e.props.selectedApiKeys)),a[n]?a=a[n][t]?v()(a,(0,d.Z)({},n,(0,d.Z)({},t,{$set:!a[n][t]}))):v()(a,(0,d.Z)({},n,(0,d.Z)({},t,{$set:!0}))):(a=v()(a,(0,d.Z)({},n,{$set:{}})),a=v()(a,(0,d.Z)({},n,(0,d.Z)({},t,{$set:!0})))),e.props.handleApiKeySelection(a)})),(0,d.Z)((0,o.Z)(e),"handleEnvChange",(function(n,t){var r={};e.props.selectedEnvVars&&(r=k({},e.props.selectedEnvVars)),r=r[n]?v()(r,(0,d.Z)({},n,{$set:!r[n]})):v()(r,(0,d.Z)({},n,{$set:!0})),e.props.handleEnvVarSelection(r)})),(0,d.Z)((0,o.Z)(e),"renderEnvSelectorTable",(function(){var n=e.props,t=n.envVars,a=n.selectedEnvVars;return(0,r.jsxs)(u.Z,{striped:!0,children:[(0,r.jsx)("thead",{children:(0,r.jsxs)("tr",{className:"dark:bg-dark-70",children:[(0,r.jsx)("th",{children:"Required"}),(0,r.jsx)("th",{children:"Key"}),(0,r.jsx)("th",{children:"Value"})]})}),(0,r.jsx)("tbody",{children:t&&t.map((function(n,t){return(0,r.jsxs)("tr",{className:"dark:even:bg-dark-90 dark:odd:bg-dark-80",children:[(0,r.jsx)("th",{children:(0,r.jsx)(f,{id:"select-".concat(n.key),checked:null===a||void 0===a?void 0:a[n.id],onChange:function(t){e.handleEnvChange(n.id,t)}})}),(0,r.jsx)("th",{children:n.key}),(0,r.jsx)("th",{children:n.value})]},"".concat(n.key,"_env_var"))}))})]})})),(0,d.Z)((0,o.Z)(e),"renderApiKeySelectorTable",(function(){var n=e.props,t=n.apiKeys,a=n.selectedApiKeys,o=n.extractEnabled;return(0,r.jsxs)(u.Z,{striped:!0,children:[(0,r.jsx)("thead",{children:(0,r.jsxs)("tr",{className:"dark:bg-dark-70",children:[(0,r.jsxs)("th",{children:["Required"," ",(0,r.jsx)(b.Z,{element:"a",href:"/courses/author-guide/BnxqxY5wY1n#required-api-keys",overlay:"Learn about Required API keys.",parentClasses:"h-4 w-4",position:y.YS6,target:"_blank",children:(0,r.jsx)(m.Z,{className:"h-3 w-3"})})]}),o&&(0,r.jsxs)("th",{children:["Extract"," ",(0,r.jsx)(b.Z,{element:"a",href:"/courses/author-guide/q20MppwKmGR#extracted-api-keys",overlay:"Learn about Extracted API keys.",parentClasses:"h-4 w-4",position:y.YS6,target:"_blank",children:(0,r.jsx)(m.Z,{className:"h-3 w-3"})})]}),(0,r.jsx)("th",{style:{maxWidth:"150px"},children:"Key"}),(0,r.jsx)("th",{style:{maxWidth:"150px"},children:"Value"}),(0,r.jsx)("th",{style:{maxWidth:"150px"},children:"Help Text"})]})}),(0,r.jsx)("tbody",{children:t&&t.map((function(n,t){var l,i;return(0,r.jsxs)("tr",{className:"dark:even:bg-dark-90 dark:odd:bg-dark-80",children:[(0,r.jsx)("th",{children:(0,r.jsx)(f,{id:j.env.REACT_APP_STANDALONE?"selenium-required-".concat(n.key):null,checked:null===a||void 0===a||null===(l=a[n.id])||void 0===l?void 0:l.required,onChange:function(t){e.handleApiKeyChange(n.id,"required",t)}})}),o&&(0,r.jsx)("th",{children:(0,r.jsx)(f,{id:j.env.REACT_APP_STANDALONE?"selenium-extract-".concat(n.key):null,checked:null===a||void 0===a||null===(i=a[n.id])||void 0===i?void 0:i.extract,onChange:function(t){e.handleApiKeyChange(n.id,"extract",t)}})}),(0,r.jsx)("th",{style:{maxWidth:"150px",overflowWrap:"break-word"},children:n.key}),(0,r.jsx)("th",{style:{maxWidth:"150px",overflowWrap:"break-word"},children:n.value}),(0,r.jsx)("th",{style:{maxWidth:"150px",overflowWrap:"break-word"},children:n.urlText})]},"".concat(n.key,"_api_keys"))}))})]})})),(0,d.Z)((0,o.Z)(e),"render",(function(){return(0,r.jsx)("div",{className:"dark:hover:text-primary-light hover:text-primary ".concat(e.props.playground?"my-2":""),children:(0,r.jsx)(b.Z,{backgroundColor:"bg-white border-white dark:bg-dark-70 dark:border-dark-70",overlay:(0,r.jsxs)(r.Fragment,{children:[(0,r.jsxs)("div",{className:"border-0 border-b-2 border-black border-solid flex items-center justify-between",children:[(0,r.jsx)("strong",{children:e.props.title}),(0,r.jsx)("button",{className:"bg-transparent p-1",onClick:function(){return e.closeOverlay()},children:(0,r.jsx)(p.Z,{className:"dark:text-gray-400 h-4 stroke-current text-black w-4"})})]}),e.props.isEnv?e.renderEnvSelectorTable():e.renderApiKeySelectorTable()]}),overlayParentClasses:"flex flex-col",overlayParentTextColorClasses:"text-black dark:text-gray-400",position:y.xRW,rootClose:!0,setRef:function(n,t){return e.closeOverlay=t},trigger:y.t4j,children:e.props.children})})})),e}return t}(c.Component);(0,d.Z)(w,"defaultProps",{apiKeys:[],selectedApiKeys:{},handleApiKeySelection:function(){return null},envVars:[],selectedEnvVars:{},handleEnvVarSelection:function(){return null},isEnv:!1,playground:!1,extractEnabled:!1});var O=w},30583:function(e,n,t){var r=t(20348),a=t(93586),o=t(64537);t(89703);function l(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?l(Object(t),!0).forEach((function(n){(0,a.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):l(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}n.Z=function(e){var n=e.children,t=e.style,a=void 0===t?{}:t,l=e.hover,s=void 0!==l&&l,d=e.condensed,c=void 0!==d&&d,u=e.bordered,p=void 0!==u&&u,h=e.responsive,g=void 0!==h&&h,f=e.striped,x=void 0!==f&&f,v=e.className,b=void 0===v?"":v,m=(0,o.Z)(e,["children","style","hover","condensed","bordered","responsive","striped","className"]);return(0,r.jsx)(r.Fragment,{children:(0,r.jsx)("table",i(i({style:i({},a),className:"w-full max-w-full edu-table ".concat(c?"edu-table-condensed":"").concat(s?" edu-table-hover ":"").concat(p?" edu-table-bordered":"").concat(x?" edu-table-striped":"").concat(g?" edu-table-responsize":""," ").concat(b)},m),{},{children:n}))})}},5825:function(e,n,t){t.d(n,{GU:function(){return F},gC:function(){return W},OP:function(){return _},X9:function(){return I},Mp:function(){return V}});var r,a,o=t(20348),l=t(30645),i=t(79003),s=t(70989),d=t(58055),c=t(31428),u=t(27018),p=t(29799),h=t(93586),g=t(89703),f=t(63048),x=t(78050),v=t(64875);function b(){return(b=Object.assign||function(e){for(var n=1;n<arguments.length;n++){var t=arguments[n];for(var r in t)Object.prototype.hasOwnProperty.call(t,r)&&(e[r]=t[r])}return e}).apply(this,arguments)}var m,y=function(e){return g.createElement("svg",b({xmlns:"http://www.w3.org/2000/svg",height:24,viewBox:"0 0 24 24",width:24},e),r||(r=g.createElement("path",{d:"M0 0h24v24H0z",fill:"none"})),a||(a=g.createElement("path",{d:"M12 2a10 10 0 100 20 10 10 0 000-20zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"})))},j=t(34560),C=t(11141),k=t(74918),Z=t(97837),w=t(16962),O=t(12006),E=t(17811),L=t(33022),S=t(54046),D={CenterLabel:L.ZP.label.withConfig({displayName:"styles__CenterLabel",componentId:"sc-1t470lf-0"})(["display:inline-flex;cursor:pointer;margin:0 15px 0 3px;.checkbox{margin-top:0px;margin-bottom:15px;}.form{margin-left:5px;border-radius:",";width:60px;}.fa-info-circle{margin:-4px 8px 0 -13px;}align-items:center;"],S.QH),CheckboxContainer:L.ZP.div.withConfig({displayName:"styles__CheckboxContainer",componentId:"sc-1t470lf-1"})([""," padding:5px;padding-left:15px;margin:5px 10px 5px 15px;border-radius:",";display:inline-block;"],{"--tw-bg-opacity":"1",backgroundColor:"rgba(255, 255, 255, var(--tw-bg-opacity))",".dark &":{"--tw-bg-opacity":"1",backgroundColor:"rgba(21, 21, 30, var(--tw-bg-opacity))"}},S.QH),DownloadLabel:L.ZP.label.withConfig({displayName:"styles__DownloadLabel",componentId:"sc-1t470lf-2"})(["display:inline-flex;align-items:center;cursor:pointer;margin:0 15px 0 3px;.checkbox{margin-top:0px;margin-bottom:15px;}.form{margin-left:5px;border-radius:",";width:60px;}.fa-info-circle{margin:-4px 8px 0 -13px;}span{margin-right:10px;margin-top:2px;}"],S.QH),DownloadLabel2:L.ZP.div.withConfig({displayName:"styles__DownloadLabel2",componentId:"sc-1t470lf-3"})(["display:inline-flex;align-items:center;cursor:pointer;margin:0 15px 0 3px;.checkbox{margin-top:0px;margin-bottom:15px;}.form{margin-left:5px;border-radius:",";width:60px;}.fa-info-circle{margin:-4px 8px 0 -13px;}span{margin-right:10px;margin-top:2px;}"],S.QH),JottedPositionOverride:L.ZP.div.withConfig({displayName:"styles__JottedPositionOverride",componentId:"sc-1t470lf-4"})(["position:relative;"])},A=t(49227),N=t(96796),P=t(28100),T=t(33212),H=t(23210),R=t(91624),K=t(73173);function M(e){var n=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}();return function(){var t,r=(0,p.Z)(e);if(n){var a=(0,p.Z)(this).constructor;t=Reflect.construct(r,arguments,a)}else t=r.apply(this,arguments);return(0,u.Z)(this,t)}}var I="javascript",V=["default","vsDark","vsLight"],_={default:"vsDark",vsDark:"vsDark",vsLight:"vsLight"},W={default:"vscode-dark",vsDark:"vscode-dark",vsLight:"vscode-light"},J=(m={},(0,h.Z)(m,j.Zs,"No Input"),(0,h.Z)(m,j.Ol,"FreeHand"),(0,h.Z)(m,j.Wz,"Upload Image"),(0,h.Z)(m,j.O2,"Text Input"),m),B="h-8 text-xs w-full rounded py-1.5 px-3 dark:bg-dark dark:text-primary-light border-none text-primary",F=function(e){(0,c.Z)(t,e);var n=M(t);function t(){var e,r;(0,i.Z)(this,t);for(var a=arguments.length,l=new Array(a),s=0;s<a;s++)l[s]=arguments[s];return r=n.call.apply(n,[this].concat(l)),(0,h.Z)((0,d.Z)(r),"OutputImageHeightRef",g.createRef()),(0,h.Z)((0,d.Z)(r),"state",{showDockerOptions:(r.props.judge||r.props.runnable||r.props.showJobsDropdown)&&(null===(e=r.props.docker.jobs)||void 0===e?void 0:e.length)>0}),(0,h.Z)((0,d.Z)(r),"getHelloWordCode",(function(){var e,n=r.props,t=n.executionConfig,a=n.executionMetadata,o=t.usercodeLanguage,l=null===a||void 0===a||null===(e=a.data)||void 0===e?void 0:e.languages;if({}.hasOwnProperty.call(l,o)){var i,s=null===l||void 0===l||null===(i=l[o])||void 0===i?void 0:i.hello_world;r.props.onMultiChange({content:s,onlyCodeChanged:!1})}})),(0,h.Z)((0,d.Z)(r),"handleSelectLanguage",(function(e){var n,t,a,o=r.props.executionMetadata,l=null===o||void 0===o||null===(n=o.data)||void 0===n?void 0:n.languages;!r.props.judge||null!==l&&void 0!==l&&null!==(t=l[e])&&void 0!==t&&t.judge||r.props.onJudgeChange(!1),!r.props.runnable||null!==l&&void 0!==l&&null!==(a=l[e])&&void 0!==a&&a.runnable||r.props.onRunnableChange(!1),r.props.onLanguageSelect(e)})),(0,h.Z)((0,d.Z)(r),"handleSelectEvaluateLanguage",(function(e){r.props.onEvaluateLanguageSelect(e)})),(0,h.Z)((0,d.Z)(r),"handleSelectTheme",(function(e){r.props.onThemeSelect(e.target.value)})),(0,h.Z)((0,d.Z)(r),"handleShowSolutionChange",(function(e){r.props.onShowSolutionChange(!!e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleEvaluateWithoutExecutionChange",(function(e){r.props.onEvaluateWithoutExecutionChange(!!e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleAllowDownloadChange",(function(e){r.props.onAllowDownloadChange(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleTreatOutputAsHTMLChange",(function(e){r.props.onTreatOutputAsHTMLChange(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"changeFileReadonlyStatus",(function(e){r.props.changeFileReadonlyStatus(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleTransformOutputChange",(function(e){var n=r.props,t=n.dispatch,a=n.lessonParams,o=n.executionConfig,l=n.onTransformOutputChange,i=n.updateOutputTransformCode;e.target.checked&&t(w.n.show(O.j_,{title:"Transform Output or Extract API keys.",confirmHandler:function(e){i(e),t(w.n.close())},executionConfig:o,lessonParams:a,defaultCode:o.outputTransformCode||C.v})),l(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handlerEnableReadOnlyApiKeys",(function(e){r.props.onEnableReadOnlyApiKeys(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleEnableHiddenCodeChange",(function(e){r.props.onEnableHiddenCodeChange(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleEnableStdinChange",(function(e){r.props.onEnableStdinChange(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleRunnableChange",(function(e){r.props.onRunnableChange(e.target.checked),e.target.checked?r.props.onMultiChange({judge:!1,runnable:!0,evaluateWithoutExecution:!1,evaluateLanguage:null}):r.props.judge||r.props.handleApiKeySelection({}),r.handleDockerJobsVisibility(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleDockerJobsVisibility",(function(e){var n;(null===(n=r.props.docker.jobs)||void 0===n?void 0:n.length)>0&&r.setState({showDockerOptions:e})})),(0,h.Z)((0,d.Z)(r),"handleJudgeChange",(function(e){e.target.checked?r.props.onMultiChange({judge:!0,runnable:!1}):r.props.onJudgeChange&&(r.props.onJudgeChange(!1),r.props.runnable||r.props.handleApiKeySelection({})),r.handleDockerJobsVisibility(e.target.checked)})),(0,h.Z)((0,d.Z)(r),"handleHighlighedLinesChange",(function(e){r.props.onHighlightedLinesChange(e.target.value)})),(0,h.Z)((0,d.Z)(r),"handleTimeLimitChange",(function(e){r.props.onTimeLimitChange(e.target.value)})),(0,h.Z)((0,d.Z)(r),"validateOutputImageHeightChange",(function(e){var n,t=e.target.value,a=t;t<150||!t?a=150:t>999&&(a=999),null!==(n=r.OutputImageHeightRef)&&void 0!==n&&n.current&&(r.OutputImageHeightRef.current.value=a),r.props.onOutputImageHeightChange(a)})),(0,h.Z)((0,d.Z)(r),"validateTimeLimitChange",(function(e){var n=e.target.value,t=n;n<1?t=1:n>55&&(t=55),r.props.onTimeLimitChange(t)})),(0,h.Z)((0,d.Z)(r),"handlePlaygroundModeChange",(function(e){e.target.checked?r.props.onMultiChange({playgroundMode:!0,judge:!1,runnable:!0,evaluateWithoutExecution:!1,evaluateLanguage:null}):r.props.playgroundMode&&r.props.onMultiChange({playgroundMode:!1,runnable:!1})})),(0,h.Z)((0,d.Z)(r),"getHelloWorldButton",(function(e){var n,t,a=r.props,l=a.executionMetadata,i=a.selectedDockerJob,s=(0,N.EE)(i),d=null===l||void 0===l||null===(n=l.data)||void 0===n?void 0:n.languages;return(0,o.jsx)(k.Z,{danger:!0,"data-testid":"hello-world-button",disabled:s,disableTrigger:s,element:"button",handleConfirm:r.getHelloWordCode,parentClasses:"inline-flex m-0 py-2 text-default",popoverTitle:"Are you sure you want to replace the existing code?",children:"Add Hello World for ".concat(null===d||void 0===d||null===(t=d[e])||void 0===t?void 0:t.title)})})),r}return(0,s.Z)(t,[{key:"componentDidUpdate",value:function(e){var n=e.docker.jobs,t=this.props.docker.jobs;if(!f.equals(n,t)){var r=(this.props.judge||this.props.runnable)&&(null===t||void 0===t?void 0:t.length)>0;this.setState({showDockerOptions:r})}}},{key:"render",value:function(){var e,n,t,r,a,i,s,d,c,u,p=this,h=this.props,g=h.executionMetadata,f=h.executionConfig,b=h.editMode,m=h.playgroundMode,j=h.showPlaygroundMode,C=h.apiKeys,k=h.selectedApiKeys,w=h.handleApiKeySelection,O=h.mainFileSelected,L=h.selectedEnvVars,S=h.handleEnvVarSelection,M=h.isFreeText,I=h.widgetVersion,V=(0,P.m)("Code",I,L,null===(e=this.props)||void 0===e||null===(n=e.docker)||void 0===n?void 0:n.envs),_=null===g||void 0===g||null===(t=g.data)||void 0===t?void 0:t.languages,W=f.timeLimit||30,F=f.outputImageHeight||A.f55,q=f.usercodeLanguage||f.language,z=(0,N.EE)(this.props.selectedDockerJob);return(0,o.jsxs)("div",{className:"edcomp-toolbar",style:{paddingBottom:"4px",margin:"0px",borderRadius:"0px"},children:[(0,o.jsx)("div",{children:(0,o.jsxs)("div",{style:{display:"inline-flex",alignItems:"center",paddingLeft:15,paddingTop:2,paddingBottom:2,marginTop:5,marginBottom:3},children:[b&&j&&(0,o.jsx)(D.CheckboxContainer,{children:(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Code Playground"}),(0,o.jsx)(v.Z,{checked:m,onChange:this.handlePlaygroundModeChange})]})}),(b||m)&&(0,o.jsxs)(D.CenterLabel,{className:"form-label",children:["Language",(0,o.jsx)(H.Z,{customButtonClass:"".concat(B," flex justify-between font-bold"),className:"ml-1 w-40",value:q,onChange:this.handleSelectLanguage,disabled:z,renderValue:function(e){var n;return(null===_||void 0===_||null===(n=_[e])||void 0===n?void 0:n.title)||""},noMargin:!0,children:(u=_,Object.keys(null!==u&&void 0!==u?u:{}).filter((function(e){return{}.hasOwnProperty.call(u,e)}))).filter((function(e){var n;return!m||(null===(n=_[e])||void 0===n?void 0:n.runnable)})).map((function(e){return(0,o.jsx)(R.Z,{fontClass:"text-xs",id:K.env.REACT_APP_STANDALONE?e:null,value:e,children:_[e].title},e)}))})]}),m&&_&&O&&(null===_||void 0===_||null===(r=_[f.language])||void 0===r?void 0:r.runnable)&&this.getHelloWorldButton(f.language),(0,o.jsx)(N.ZP,{docker:this.props.docker,dockerType:T.a5.GENERAL,selectedDockerJob:this.props.selectedDockerJob,onDockerJobChange:this.props.onDockerJobChanged,visibility:m&&this.props.showJobsDropdown&&!M,dropdownStyle:{fontSize:"12px"}}),z&&(null===(a=this.props.docker)||void 0===a||null===(i=a.envs)||void 0===i?void 0:i.length)>0&&(0,o.jsx)(Z.Z,{title:"Environment Vars",envVars:this.props.docker.envs,selectedEnvVars:V,handleEnvVarSelection:S,isEnv:!0,children:(0,o.jsx)(D.CheckboxContainer,{children:(0,o.jsx)(D.CenterLabel,{className:"form-label",children:"Select Env Vars"})})}),(this.props.runnable||this.props.judge||this.props.playgroundMode)&&C&&C.length>0&&(0,o.jsx)(Z.Z,{title:"API Keys",apiKeys:C,selectedApiKeys:k,handleApiKeySelection:w,playground:this.props.playgroundMode,extractEnabled:!0,children:(0,o.jsx)(D.CheckboxContainer,{children:(0,o.jsx)(D.CenterLabel,{className:"form-label",children:"Select API Keys"})})}),b&&!m&&(0,o.jsxs)(o.Fragment,{children:[this.props.specialInput&&(this.props.runnable||this.props.judge)&&(0,o.jsxs)(D.CenterLabel,{className:"form-label",children:["Special Input",(0,o.jsx)(H.Z,{customButtonClass:"".concat(B," flex justify-between font-bold"),className:"ml-1 w-32",noMargin:!0,onChange:this.props.onSpecialInputSelect,value:this.props.specialInput,renderValue:function(e){return J[e]},children:Object.entries(J).map((function(e){var n=(0,l.Z)(e,2),t=n[0],r=n[1];return(0,o.jsx)(R.Z,{"data-testid":t,value:t,fontClass:"text-xs",children:r})}))})]}),(0,o.jsx)(N.ZP,{className:"mr-4",docker:this.props.docker,dockerType:T.a5.GENERAL,selectedDockerJob:this.props.selectedDockerJob,onDockerJobChange:this.props.onDockerJobChanged,visibility:this.state.showDockerOptions&&!M,dropdownStyle:{fontSize:"12px"}}),(this.props.runnable||this.props.judge)&&(0,o.jsxs)(D.CenterLabel,{className:"form-label",children:["Time Limit (secs)",(0,o.jsx)("input",{className:"form ".concat(B," no-outline"),type:"number",onChange:this.handleTimeLimitChange,onBlur:this.validateTimeLimitChange,value:W})]}),(0,o.jsx)(E.Z,{value:this.props.highlightedLines,onChangeLines:this.handleHighlighedLinesChange})]})]})}),b&&!m&&(0,o.jsxs)(o.Fragment,{children:[(0,o.jsxs)(D.CheckboxContainer,{children:[(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Execute"}),(0,o.jsx)(v.Z,{disabled:!(null!==_&&void 0!==_&&null!==(s=_[q])&&void 0!==s&&s.runnable),checked:this.props.runnable,onChange:this.handleRunnableChange})]}),_&&O&&(null===_||void 0===_||null===(d=_[q])||void 0===d?void 0:d.runnable)&&this.getHelloWorldButton(q)]}),!this.props.hideOutputHeight&&(this.props.runnable||this.props.judge)&&(0,o.jsx)(D.CheckboxContainer,{children:(0,o.jsxs)(D.CenterLabel,{className:"form-label",children:["Output Image Height (px)",(0,o.jsx)("input",{ref:this.OutputImageHeightRef,maxLength:3,className:"form ".concat(B," no-outline"),type:"number",onBlur:this.validateOutputImageHeightChange,defaultValue:F})]})}),(0,o.jsx)(D.CheckboxContainer,{children:(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Exercise"}),(0,o.jsx)(v.Z,{disabled:!(null!==_&&void 0!==_&&null!==(c=_[q])&&void 0!==c&&c.judge),checked:this.props.judge,onChange:this.handleJudgeChange})]})}),(0,o.jsxs)(D.CheckboxContainer,{children:[this.props.runnable?(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Hidden Code"}),(0,o.jsx)(v.Z,{checked:this.props.enableHiddenCode,onChange:this.handleEnableHiddenCodeChange})]}):null,this.props.runnable?(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Stdin"}),(0,o.jsx)(v.Z,{checked:this.props.enableStdin,onChange:this.handleEnableStdinChange})]}):null,this.props.runnable?(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Treat Output as HTML"}),(0,o.jsx)(v.Z,{checked:this.props.treatOutputAsHTML,onChange:this.handleTreatOutputAsHTMLChange})]}):null,this.props.runnable?(0,o.jsxs)(D.DownloadLabel2,{className:"form-label",children:[(0,o.jsx)("span",{cursor:"pointer",onClick:function(){p.handleTransformOutputChange({target:{checked:!0}})},children:"Transform Output / Extract API Keys"}),(0,o.jsx)(v.Z,{checked:this.props.executionConfig.transformOutput||!1,onChange:this.handleTransformOutputChange})]}):null,this.props.runnable&&this.props.readOnly&&this.props.onEnableReadOnlyApiKeys?(0,o.jsxs)(D.DownloadLabel2,{className:"form-label",children:[(0,o.jsx)("span",{children:"Read Only API Keys"}),(0,o.jsx)(v.Z,{checked:this.props.readOnlyApiKeys||!1,onChange:this.handlerEnableReadOnlyApiKeys})]}):null,this.props.judge?(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Solution"}),(0,o.jsx)(v.Z,{checked:this.props.showSolution,onChange:this.handleShowSolutionChange})]}):null,this.props.judge?(0,o.jsxs)("label",{className:"cursor-pointer inline-flex items-center ml-1 mr-4 my-0",children:[(0,o.jsx)("span",{children:"Evaluate in Another Language "}),(0,o.jsx)(x.Z,{parentClasses:"mr-2",position:A.YS6,overlay:"Access the user code as edTestMetadata.userCode",children:(0,o.jsx)(y,{className:"fill-current h-4 w-4"})}),(0,o.jsx)(v.Z,{checked:this.props.evaluateWithoutExecution,onChange:this.handleEvaluateWithoutExecutionChange})]}):null,this.props.evaluateWithoutExecution&&(0,o.jsxs)(D.CenterLabel,{className:"form-label",children:["Language for evaluation",(0,o.jsx)(H.Z,{customButtonClass:"".concat(B," flex justify-between font-bold"),className:"ml-1 w-44",value:f.language,onChange:this.handleSelectEvaluateLanguage,noMargin:!0,renderValue:function(e){return _[e].title},children:Object.entries(_).filter((function(e){var n=(0,l.Z)(e,1)[0];return!!_[n].judge})).map((function(e){var n=(0,l.Z)(e,2),t=n[0],r=n[1];return(0,o.jsx)(R.Z,{fontClass:"text-xs",value:t,children:r.title},t)}))})]}),(0,o.jsxs)(D.DownloadLabel,{className:"form-label",children:[(0,o.jsx)("span",{children:"Downloadable"}),(0,o.jsx)(v.Z,{checked:this.props.allowDownload,onChange:this.handleAllowDownloadChange})]})]}),(0,o.jsxs)(x.Z,{element:"span",parentClasses:"cursor-pointer bg-white dark:bg-dark inline-flex items-center ml-4 mr-3 my-1 p-2 px-5 rounded",position:A.YS6,overlay:!(this.props.runnable||this.props.judge)&&"Files are Read Only if not executable or exercise",children:[(0,o.jsx)("span",{className:"mr-2",children:"Mark current file as read-only"}),(0,o.jsx)(v.Z,{checked:!this.props.runnable&&!this.props.judge||this.props.readOnly,onChange:this.changeFileReadonlyStatus,disabled:!this.props.runnable&&!this.props.judge})]})]})]})}}]),t}(g.Component);(0,h.Z)(F,"defaultProps",{docker:{jobs:[]},selectedDockerJob:{},onDockerJobChanged:function(){},specialInput:"",playgroundMode:!1,showPlaygroundMode:!1,runnable:!1,judge:!1,allowDownload:!1,treatOutputAsHTML:!1,enableHiddenCode:!1,enableStdin:!1,showSolution:!1,evaluateWithoutExecution:!1,apiKeys:null,selectedApiKeys:{},selectedEnvVars:{},widgetVersion:null,handleApiKeySelection:function(){},handleEnvVarSelection:function(){},readOnly:!1,showJobsDropdown:!1,hideOutputHeight:!1,isFreeText:!1})},17811:function(e,n,t){var r=t(20348),a=t(30645),o=t(89703);n.Z=function(e){var n=e.onChangeLines,t=e.value,l=o.useRef(null),i=o.useState(!1),s=(0,a.Z)(i,2),d=s[0],c=s[1];return o.useEffect((function(){var e;return d&&(null===(e=l.current)||void 0===e?void 0:e.focus())}),[d]),d?(0,r.jsx)("textarea",{className:"border-none dark:bg-dark dark:placeholder-gray-600 dark:text-primary-light h-14 mr-4 no-outline px-3 py-1.5 resize-none rounded text-primary text-xs w-52",placeholder:"Enter line ranges to highlight",rows:3,cols:25,ref:function(e){return l.current=e},defaultValue:t,onBlur:function(e){e.target.value!==t&&n(e),c(!1)}}):(0,r.jsx)("span",{onClick:function(){return c(!0)},className:"cursor-pointer dark:hover:text-primary-light duration-200 hover:text-primary transition-all",children:"Highlight lines"})}},11141:function(e,n,t){t.d(n,{v:function(){return r}});var r="function outputTransform(stdout, stderr) {\n  // Transform output or perform API key extraction.\n  const apiKeys = {};\n  return { apiKeys, stdout, stderr };\n}"},28100:function(e,n,t){t.d(n,{m:function(){return i},t:function(){return s}});var r=t(93586),a=t(786),o=t.n(a),l=t(49227),i=function(e,n,t,a){var i=t;return 0===Object.keys(t).length&&(n<l.hoB[e]||!n&&"TerminalWidget"===e)&&0===Object.keys(t).length&&(null===a||void 0===a||a.forEach((function(e){i=o()(i,(0,r.Z)({},e.id,{$set:!0}))}))),i},s=function(e,n){return((null===e||void 0===e?void 0:e.envs)||[]).filter((function(e){return!e.value&&(null===n||void 0===n?void 0:n[e.id])})).map((function(e){return e.key}))}}}]);
//# sourceMappingURL=5825-cd8689e93cc3c27e36e2.js.map