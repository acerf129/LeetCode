"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[68457],{68457:function(t,e,o){var r=o(20348),a=o(32868),s=o(79003),i=o(70989),l=o(58055),n=o(31428),d=o(27018),u=o(29799),p=o(93586),c=o(89703),h=o(78854),v=o(12101),g=o(59290),f=o(96807),m=o(14972),k=o(93636),C=o(46052),y=o(33027),P=o(82546),E=o(52558),_=o(49227),L=o(18147),A=o(83200);function S(t){var e=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(t){return!1}}();return function(){var o,r=(0,u.Z)(t);if(e){var a=(0,u.Z)(this).constructor;o=Reflect.construct(r,arguments,a)}else o=r.apply(this,arguments);return(0,d.Z)(this,o)}}var b={m:5001,blog:5002,enterprise:5003},Z=["author","collab","ref"];e.Z=function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0],e=arguments.length>1&&void 0!==arguments[1]&&arguments[1],o=!(arguments.length>2&&void 0!==arguments[2])||arguments[2],d=arguments.length>3&&void 0!==arguments[3]&&arguments[3];function u(o){var r,a,s,i,l,n,d,u,p,c,h,v,g,f,m,k=o.author.work,C=o.userConfig,y=o.reader,P=y.featured,E=y.tracks,_=y.shots,L=y.editorPages,A=o.search.filter,S=o.user,b=S.info,Z=S.courseCompletion,T=o.user,F=(null===P||void 0===P||null===(r=P.data)||void 0===r?void 0:r.summaries)||[],R=(null===E||void 0===E||null===(a=E.data)||void 0===a?void 0:a.tracks)||[],I=(null===_||void 0===_||null===(s=_.data)||void 0===s?void 0:s.edpresso_shots)||[],w=(null===L||void 0===L||null===(i=L.data)||void 0===i?void 0:i.editor_pages)||[],q=!1,W=!1;t&&!1===k.loading&&k.loaded&&(F=k.data.work_summaries),!t&&!1===P.loading&&P.loaded&&(F=P.data.summaries,p=P.data.cursor,h=P.data.page_size),g=e?null===_||void 0===_||null===(l=_.data)||void 0===l?void 0:l.more:null===P||void 0===P||null===(n=P.data)||void 0===n?void 0:n.more,!1===E.loading&&E.loaded&&(R=E.data.tracks,v=E.data.cursor,q=E.data.more),!1===_.loading&&_.loaded&&(I=_.data.edpresso_shots,p=_.data.cursor,h=_.data.page_size),!1===L.loading&&L.loaded&&(w=L.data.pages,c=L.data.cursor,W=L.data.more),t?(d=k.loading||!1,u=k.loaded||!1):(d=P.loading||_.loading||L.loading||!1,u=P.loaded||_.loaded||L.loaded||!1),f=E.loading||!1,m=E.loaded||!1;var D=T.info.loaded||T.info.loggedOut;return{articles:F,trackSummaries:R,shotSummaries:I,editorPageSummaries:w,editorPagesCursor:c,moreEditorPages:W,userInfo:b.data||{},userInfoLoaded:D,contentLoading:d,contentLoaded:u,courseCompletion:null!==Z&&void 0!==Z?Z:{},cursor:p,PAGE_SIZE:h,tracksCursor:v,tracksPageSize:undefined,moreTracks:q,more:g,filterType:A,tracksLoading:f,tracksLoaded:m,constantsLoaded:!C.loading&&!!C.loaded}}var T=function(t){return{dispatch:t,getArticles:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[],r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";return t(f.s.load(e,o,r))},getEarlyAccessArticles:function(){return t(f.s.loadEarlyAccess())},getTracks:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:[],a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:3,s=arguments.length>4&&void 0!==arguments[4]?arguments[4]:"";return t(m.u.load(e,o,r,a,s))},getShots:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[],a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";return t(k.W.load(e,r,a,o))},getEditorPages:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[],r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:v.ZP.MARKETING_PAGE,a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"";return t(C.aE.load(e,o,r,a))},getAllTags:function(){return t(y.P.load())},loadAllCoursesCompletion:function(e,o){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},a=arguments.length>3?arguments[3]:void 0;return t(P.x.load(e,o,r,a))},resetCourseCompletion:function(){return t(P.x.reset())}}};return function(v){var P=(0,h.$j)(u,T)(function(u){(0,n.Z)(h,u);var c=S(h);function h(){var r;(0,s.Z)(this,h);for(var a=arguments.length,i=new Array(a),n=0;n<a;n++)i[n]=arguments[n];return r=c.call.apply(c,[this].concat(i)),(0,p.Z)((0,l.Z)(r),"state",{workFilter:Z[Number(r.props.router.query.tabIndex)||0],loadData:!1,isPathDashboard:r.props.router.asPath.startsWith("/paths-dashboard")}),(0,p.Z)((0,l.Z)(r),"completion",void 0),(0,p.Z)((0,l.Z)(r),"getRelatedPageData",(function(){if(e)r.getShotsData();else if(d){var o=r.props.router.query.pageType;r.props.dispatch(C.aE.clear()),r.props.dispatch(C.aE.load("",[],b[o]))}else r.props.resetCourseCompletion(),r.props.dispatch(m.u.clear()),r.props.dispatch(f.s.clear()),r.getCourseSummaries(),!t&&r.props.userInfoLoaded&&r.getTrackSummaries(),r.completion=!0})),(0,p.Z)((0,l.Z)(r),"getTrackSummaries",(function(){r.props.dispatch(m.u.load("",null,[],3,""))})),(0,p.Z)((0,l.Z)(r),"getCourseSummaries",(function(){var e=r.props,o=e.router,a=e.userInfo,s=e.dispatch,i=e.filterType;if(e.userInfoLoaded){var l,n;if(o.asPath.startsWith("/explore/".concat(_.Oqp.FREE.toLowerCase()))&&a.user_id&&!t)return void(a.has_early_access?(s(L.R.setFilter(_.Oqp.EARLY_ACCESS)),o.push("/explore/".concat(_.Oqp.EARLY_ACCESS))):a.is_user_subscribed?(s(L.R.setFilter(_.Oqp.ALL.toLowerCase())),o.push("/explore")):s(f.s.load("",[],o.query.selectedFilter||i)));var d=null===(l=r.props.router)||void 0===l||null===(n=l.query)||void 0===n?void 0:n.selectedFilter;if(t||d!==_.Oqp.EARLY_ACCESS){var u;!t&&o.asPath.startsWith("/explore/".concat(_.Oqp.FREE.toLowerCase()))&&s(L.R.setFilter(_.Oqp.FREE.toLowerCase()));var p=Z[Number(r.props.router.query.tabIndex)],c=!!r.props.userInfo.can_view_beta_features||(null===(u=r.props.userInfo.email)||void 0===u?void 0:u.includes("educative.io"));t?r.state.isPathDashboard?c?r.props.dispatch(g.B.load("path")):r.getCollabWork():r.props.dispatch(g.B.load(p)).then((function(){return r.getCollabWork()})):r.props.dispatch(f.s.load("",[],d||r.props.filterType))}else s(f.s.loadEarlyAccess()),s(L.R.setFilter(_.Oqp.EARLY_ACCESS))}})),(0,p.Z)((0,l.Z)(r),"setWorkFilter",(function(t){r.setState({workFilter:t,loadData:!0})})),(0,p.Z)((0,l.Z)(r),"setCompletion",(function(t){r.completion=t})),(0,p.Z)((0,l.Z)(r),"getShotsData",(function(){r.props.dispatch(k.W.clear());var t="all"===r.props.filterType?"draft":o||"published"!==r.props.filterType?r.props.filterType:"published-self";r.props.dispatch(k.W.load("",[],t,o)),r.props.dispatch(y.P.clear()),r.props.dispatch(y.P.load("",[]))})),(0,p.Z)((0,l.Z)(r),"getFilterType",(function(t){return e&&"all"===t?"draft":t})),r}return(0,i.Z)(h,[{key:"componentDidMount",value:function(){this.props.userInfoLoaded&&this.getRelatedPageData()}},{key:"shouldComponentUpdate",value:function(o){var r,s,i,l,n,u=this;if(this.props.router.asPath!==o.router.asPath&&"/teach"===o.router.pathname){this.props.dispatch(g.B.clear());var p=o.router.asPath.startsWith("/paths-dashboard")?"path":"author";this.props.dispatch(g.B.load(p)).then((function(){return u.state.isPathDashboard?u.getPrivatePaths():u.getCollabWork()}))}var c=o.PAGE_SIZE;if(!o.contentLoading&&o.contentLoaded&&Object.keys(null!==(r=o.userInfo)&&void 0!==r?r:{}).length&&this.completion){var h,v,m;if(t)this.props.loadAllCoursesCompletion([].concat((0,a.Z)(null===(h=o.articles)||void 0===h?void 0:h.author_work),(0,a.Z)(null===(v=o.articles)||void 0===v?void 0:v.ref_work),[null===(m=o.articles)||void 0===m?void 0:m.collab_work]),o.userInfo.user_id);else{var P=o.articles.length%c===0?c:o.articles.length%c,E=o.articles.slice(o.articles.length-P,o.articles.length);this.props.loadAllCoursesCompletion(E,o.userInfo.user_id,o.courseCompletion)}this.setCompletion(!1)}if(this.props.filterType!==o.filterType||(null===(s=this.props.router)||void 0===s||null===(i=s.query)||void 0===i?void 0:i.selectedFilter)!==(null===(l=o.router)||void 0===l||null===(n=l.query)||void 0===n?void 0:n.selectedFilter)){var A=this.props,S=A.getArticles,Z=A.getEarlyAccessArticles,T=A.dispatch,F=A.resetCourseCompletion,R=A.getShots,I=A.getAllTags,w=A.userInfo,q=A.router;if(e){T(k.W.clear()),T(y.P.clear());var W="published"===o.filterType?"published-self":o.filterType;console.trace(),R("",[],W),I()}else{if(!d){var D,O,x,B;if((null===(D=this.props.router)||void 0===D||null===(O=D.query)||void 0===O?void 0:O.selectedFilter)!==(null===(x=o.router)||void 0===x||null===(B=x.query)||void 0===B?void 0:B.selectedFilter)){var Y,z;if(w.has_early_access&&(null===(Y=o.router)||void 0===Y||null===(z=Y.query)||void 0===z?void 0:z.selectedFilter)===_.Oqp.FREE.toLowerCase())return T(L.R.setFilter(_.Oqp.EARLY_ACCESS)),q.push("/explore/".concat(_.Oqp.EARLY_ACCESS)),!1;var N=o.router.query.selectedFilter;T(f.s.clear()),F(),N===_.Oqp.EARLY_ACCESS?Z():S("",[],N||o.filterType),this.setCompletion(!0)}return!1}var j=this.props.router.query.pageType;T(C.aE.clear()),this.props.dispatch(C.aE.load("",[],b[j]))}}return!(this.props.articles.length===o.articles.length&&this.props.contentLoading===o.contentLoading&&!o.trackSummaries.length&&this.props.tracksLoading!==o.tracksLoading)}},{key:"componentDidUpdate",value:function(e){var o,r,a,s,i,l,n=null===(o=e.userInfo)||void 0===o?void 0:o.user_id,d=null===(r=this.props.userInfo)||void 0===r?void 0:r.user_id;(this.props.router.asPath!==e.router.asPath&&this.setState({isPathDashboard:this.props.router.asPath.startsWith("/paths-dashboard")}),(!n&&d||!e.userInfoLoaded&&this.props.userInfoLoaded)&&this.getRelatedPageData(),t&&this.state.loadData&&!this.props.contentLoading)&&("author"!==this.state.workFilter||((null===(a=this.props.articles)||void 0===a?void 0:a.author_work)||[]).length||this.getAuthorWork(),"collab"!==this.state.workFilter||((null===(s=this.props.articles)||void 0===s?void 0:s.collab_work)||[]).length||this.getCollabWork(),"ref"!==this.state.workFilter||((null===(i=this.props.articles)||void 0===i?void 0:i.ref_work)||[]).length||this.getRefWork(),"private"!==this.state.workFilter||((null===(l=this.props.articles)||void 0===l?void 0:l.private_work)||[]).length||this.getPrivatePaths(),this.setState({loadData:!1}))}},{key:"componentWillUnmount",value:function(){e?this.props.dispatch(k.W.clear()):d?this.props.dispatch(C.aE.clear()):this.props.dispatch(m.u.clear())}},{key:"getAuthorWork",value:function(){this.props.dispatch(g.B.load("author",this.props.articles))}},{key:"getCollabWork",value:function(){this.props.dispatch(g.B.load("collab",this.props.articles))}},{key:"getRefWork",value:function(){this.props.dispatch(g.B.load("ref",this.props.articles))}},{key:"getPrivatePaths",value:function(){if(this.state.isPathDashboard){var t,e,o,r=this.props,a=r.userInfo,s=r.dispatch,i=r.articles,l=null===a||void 0===a||null===(t=a.enterprise)||void 0===t||null===(e=t.organizations)||void 0===e||null===(o=e.find((function(t){return t.can_create_private_content})))||void 0===o?void 0:o.organization_id;l&&s(g.B.loadPrivatePaths(l,i))}}},{key:"render",value:function(){var t=this.props,e=t.articles,o=t.trackSummaries,a=t.shotSummaries,s=t.editorPageSummaries,i=t.dispatch,l=t.userInfo,n=t.userInfoLoaded,d=t.tracksLoading,u=t.tracksLoaded,p=t.contentLoading,c=t.contentLoaded,h=t.courseCompletion,g=t.cursor,f=t.editorPagesCursor,m=t.more,k=t.moreTracks,C=t.moreEditorPages,y=t.getArticles,P=t.getTracks,_=t.getEditorPages,L=t.getShots,A=t.getAllTags,S=t.loadAllCoursesCompletion,b=t.filterType,Z=t.tracksCursor,T=t.match,F=t.constantsLoaded,R=t.ssrShots;return(0,r.jsx)(v,{setCompletion:this.setCompletion,courseCompletion:h,articles:e,tracks:o,shots:a,ssrShots:R,editorPages:s,editorPagesCursor:f,moreEditorPages:C,dispatch:i,userInfo:l,userInfoLoaded:n,loading:p,loaded:c,tracksLoading:d,tracksLoaded:u,cursor:g,tracksCursor:Z,more:m,moreTracks:k,getArticles:y,getTracks:P,getEditorPages:_,getAllTags:A,getShots:L,loadAllCoursesCompletion:S,filterType:this.getFilterType(b),match:T,setWorkFilter:this.setWorkFilter,isPathDashboard:this.state.isPathDashboard,constantsLoaded:F,children:(0,r.jsx)(E.Z,{loading:p})})}}]),h}(c.Component));return(0,A.withRouter)(P)}}}}]);
//# sourceMappingURL=68457-e4403fc68b7a7c27f932.js.map