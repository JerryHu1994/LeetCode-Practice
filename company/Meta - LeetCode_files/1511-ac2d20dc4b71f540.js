(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1511],{27459:function(e,t,n){"use strict";const o=n(73094),r=n(49249);function*a(e){let t=1e3;for(;;){const n=e/t;if(n<1)return;yield n,t*=1e3}}function i(e,t){var n;const i=t?Object.assign(Object.assign({},o.defaultOptions),t):o.defaultOptions;if(!Array.isArray(i.units)||!i.units.length)throw new Error("Option `units` must be a non-empty array");let s=r.parseValue(e);const u=s<0?"-":"";s=Math.abs(s);let c=0;for(const o of a(s))s=o,c+=1;if(c>=i.units.length)return e.toString();let l=r.roundTo(s,i.precision);for(const o of a(l))l=o,c+=1;const h=null!==(n=i.units[c])&&void 0!==n?n:"",d=i.lowercase?h.toLowerCase():h,f=i.space?" ":"";return`${u}${l.toString().replace(o.defaultOptions.decimalSeparator,i.decimalSeparator)}${f}${d}`}t.ZP=i},73094:function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.defaultOptions=void 0,t.defaultOptions={decimalSeparator:".",lowercase:!1,precision:1,space:!1,units:["","K","M","B","T","P","E"]}},49249:function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.roundTo=t.parseValue=void 0,t.parseValue=function(e){const t=parseFloat(null===e||void 0===e?void 0:e.toString());if(isNaN(t))throw new Error("Input value is not a number");if(t>Number.MAX_SAFE_INTEGER||t<Number.MIN_SAFE_INTEGER)throw new RangeError("Input value is outside of safe integer range");return t},t.roundTo=function(e,t){if(!Number.isFinite(e))throw new Error("Input value is not a finite number");if(!Number.isInteger(t)||t<0)throw new Error("Precision is not a positive integer");return Number.isInteger(e)?e:parseFloat(e.toFixed(t))}},27011:function(e,t,n){e.exports=function(e,t){"use strict";function n(e){return e&&"object"==typeof e&&"default"in e?e:{default:e}}var o=n(e),r=n(t);function a(e,t){for(var n=0;n<t.length;n++){var o=t[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function s(){return(s=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e}).apply(this,arguments)}function u(e,t){var n,o=Object.keys(e);return Object.getOwnPropertySymbols&&(n=Object.getOwnPropertySymbols(e),t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,n)),o}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?u(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):u(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e){return(l=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function h(e,t){return(h=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function d(e,t){if(null==e)return{};var n,o=function(e,t){if(null==e)return{};for(var n,o={},r=Object.keys(e),a=0;a<r.length;a++)n=r[a],0<=t.indexOf(n)||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols)for(var r=Object.getOwnPropertySymbols(e),a=0;a<r.length;a++)n=r[a],0<=t.indexOf(n)||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n]);return o}function f(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function p(t){var n=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}();return function(){var e,o,r=l(t);return!(o=n?(e=l(this).constructor,Reflect.construct(r,arguments,e)):r.apply(this,arguments))||"object"!=typeof o&&"function"!=typeof o?f(this):o}}function g(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e)){var n=[],o=!0,r=!1,a=void 0;try{for(var i,s=e[Symbol.iterator]();!(o=(i=s.next()).done)&&(n.push(i.value),!t||n.length!==t);o=!0);}catch(e){r=!0,a=e}finally{try{o||null==s.return||s.return()}finally{if(r)throw a}}return n}}(e,t)||v(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function v(e,t){if(e){if("string"==typeof e)return m(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?m(e,t):void 0}}function m(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,o=new Array(t);n<t;n++)o[n]=e[n];return o}function b(e,t){return new Promise((function(n,o){var r,a=new Image;a.onload=function(){return n(a)},a.onerror=o,0==(null!==(r=e)&&!!r.match(/^\s*data:([a-z]+\/[a-z]+(;[a-z-]+=[a-z-]+)?)?(;base64)?,[a-z0-9!$&',()*+;=\-._~:@/?%\s]*\s*$/i))&&t&&(a.crossOrigin=t),a.src=e}))}var y,w=!("undefined"==typeof window||"undefined"==typeof navigator||!("ontouchstart"in window||0<navigator.msMaxTouchPoints)),M="undefined"!=typeof File,O={touch:{react:{down:"onTouchStart",mouseDown:"onMouseDown",drag:"onTouchMove",move:"onTouchMove",mouseMove:"onMouseMove",up:"onTouchEnd",mouseUp:"onMouseUp"},native:{down:"touchstart",mouseDown:"mousedown",drag:"touchmove",move:"touchmove",mouseMove:"mousemove",up:"touchend",mouseUp:"mouseup"}},desktop:{react:{down:"onMouseDown",drag:"onDragOver",move:"onMouseMove",up:"onMouseUp"},native:{down:"mousedown",drag:"dragStart",move:"mousemove",up:"mouseup"}}},I=w?O.touch:O.desktop,E="undefined"!=typeof window&&window.devicePixelRatio?window.devicePixelRatio:1,T={x:.5,y:.5},C=function(){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&h(e,t)}(u,r.default.Component);var e,t,n,o=p(u);function u(e){var t;return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,u),i(f(t=o.call(this,e)),"state",{drag:!1,my:null,mx:null,image:T}),i(f(t),"handleImageReady",(function(e){var n=t.getInitialSize(e.width,e.height);n.resource=e,n.x=.5,n.y=.5,n.backgroundColor=t.props.backgroundColor,t.setState({drag:!1,image:n},t.props.onImageReady),t.props.onLoadSuccess(n)})),i(f(t),"clearImage",(function(){t.canvas.getContext("2d").clearRect(0,0,t.canvas.width,t.canvas.height),t.setState({image:T})})),i(f(t),"handleMouseDown",(function(e){(e=e||window.event).preventDefault(),t.setState({drag:!0,mx:null,my:null})})),i(f(t),"handleMouseUp",(function(){t.state.drag&&(t.setState({drag:!1}),t.props.onMouseUp())})),i(f(t),"handleMouseMove",(function(e){var n,o,r,a,i,s,u,l,h,d,f,p,g,v,m,b;e=e||window.event,!1!==t.state.drag&&(e.preventDefault(),r={mx:n=e.targetTouches?e.targetTouches[0].pageX:e.clientX,my:o=e.targetTouches?e.targetTouches[0].pageY:e.clientY},b=t.props.rotate,b=(b%=360)<0?b+360:b,t.state.mx&&t.state.my&&(a=t.state.mx-n,i=t.state.my-o,s=t.state.image.width*t.props.scale,u=t.state.image.height*t.props.scale,h=(l=t.getCroppingRect()).x,d=l.y,h*=s,d*=u,f=function(e){return e*(Math.PI/180)},p=Math.cos(f(b)),v=d+-a*(g=Math.sin(f(b)))+i*p,m={x:(h+a*p+i*g)/s+1/t.props.scale*t.getXScale()/2,y:v/u+1/t.props.scale*t.getYScale()/2},t.props.onPositionChange(m),r.image=c(c({},t.state.image),m)),t.setState(r),t.props.onMouseMove(e))})),i(f(t),"setCanvas",(function(e){t.canvas=e})),t.canvas=null,t}return e=u,(t=[{key:"componentDidMount",value:function(){this.props.disableHiDPIScaling&&(E=1);var e,t,n=this.canvas.getContext("2d");this.props.image&&this.loadImage(this.props.image),this.paint(n),document&&(e=!!function(){var e=!1;try{var t=Object.defineProperty({},"passive",{get:function(){e=!0}});window.addEventListener("test",t,t),window.removeEventListener("test",t,t)}catch(t){e=!1}return e}()&&{passive:!1},t=I.native,document.addEventListener(t.move,this.handleMouseMove,e),document.addEventListener(t.up,this.handleMouseUp,e),w&&(document.addEventListener(t.mouseMove,this.handleMouseMove,e),document.addEventListener(t.mouseUp,this.handleMouseUp,e)))}},{key:"componentDidUpdate",value:function(e,t){this.props.image&&this.props.image!==e.image||this.props.width!==e.width||this.props.height!==e.height||this.props.backgroundColor!==e.backgroundColor?this.loadImage(this.props.image):this.props.image||t.image===T||this.clearImage();var n=this.canvas.getContext("2d");n.clearRect(0,0,this.canvas.width,this.canvas.height),this.paint(n),this.paintImage(n,this.state.image,this.props.border),e.image===this.props.image&&e.width===this.props.width&&e.height===this.props.height&&e.position===this.props.position&&e.scale===this.props.scale&&e.rotate===this.props.rotate&&t.my===this.state.my&&t.mx===this.state.mx&&t.image.x===this.state.image.x&&t.image.y===this.state.image.y&&t.backgroundColor===this.state.backgroundColor||this.props.onImageChange()}},{key:"componentWillUnmount",value:function(){var e;document&&(e=I.native,document.removeEventListener(e.move,this.handleMouseMove,!1),document.removeEventListener(e.up,this.handleMouseUp,!1),w&&(document.removeEventListener(e.mouseMove,this.handleMouseMove,!1),document.removeEventListener(e.mouseUp,this.handleMouseUp,!1)))}},{key:"isVertical",value:function(){return!this.props.disableCanvasRotation&&this.props.rotate%180!=0}},{key:"getBorders",value:function(e){var t=0<arguments.length&&void 0!==e?e:this.props.border;return Array.isArray(t)?t:[t,t]}},{key:"getDimensions",value:function(){var e=this.props,t=e.width,n=e.height,o=e.rotate,r=e.border,a={},i=g(this.getBorders(r),2),s=i[0],u=i[1],c=t,l=n;return this.isVertical()?(a.width=l,a.height=c):(a.width=c,a.height=l),a.width+=2*s,a.height+=2*u,{canvas:a,rotate:o,width:t,height:n,border:r}}},{key:"getImage",value:function(){var e=this.getCroppingRect(),t=this.state.image;e.x*=t.resource.width,e.y*=t.resource.height,e.width*=t.resource.width,e.height*=t.resource.height;var n=document.createElement("canvas");this.isVertical()?(n.width=e.height,n.height=e.width):(n.width=e.width,n.height=e.height);var o=n.getContext("2d");return o.translate(n.width/2,n.height/2),o.rotate(this.props.rotate*Math.PI/180),o.translate(-n.width/2,-n.height/2),this.isVertical()&&o.translate((n.width-n.height)/2,(n.height-n.width)/2),t.backgroundColor&&(o.fillStyle=t.backgroundColor,o.fillRect(-e.x,-e.y,t.resource.width,t.resource.height)),o.drawImage(t.resource,-e.x,-e.y),n}},{key:"getImageScaledToCanvas",value:function(){var e=this.getDimensions(),t=e.width,n=e.height,o=document.createElement("canvas");return this.isVertical()?(o.width=n,o.height=t):(o.width=t,o.height=n),this.paintImage(o.getContext("2d"),this.state.image,0,1),o}},{key:"getXScale",value:function(){var e=this.props.width/this.props.height,t=this.state.image.width/this.state.image.height;return Math.min(1,e/t)}},{key:"getYScale",value:function(){var e=this.props.height/this.props.width,t=this.state.image.height/this.state.image.width;return Math.min(1,e/t)}},{key:"getCroppingRect",value:function(){var e=this.props.position||{x:this.state.image.x,y:this.state.image.y},t=1/this.props.scale*this.getXScale(),n=1/this.props.scale*this.getYScale(),o={x:e.x-t/2,y:e.y-n/2,width:t,height:n},r=0,a=1-o.width,i=0,s=1-o.height;return(this.props.disableBoundaryChecks||1<t||1<n)&&(r=-o.width,i=-o.height,s=a=1),c(c({},o),{},{x:Math.max(r,Math.min(o.x,a)),y:Math.max(i,Math.min(o.y,s))})}},{key:"loadImage",value:function(e){var t;M&&e instanceof File?this.loadingImage=(t=e,new Promise((function(e,n){var o=new FileReader;o.onload=function(t){try{var o=b(t.target.result);e(o)}catch(t){n(t)}},o.readAsDataURL(t)})).then(this.handleImageReady).catch(this.props.onLoadFailure)):"string"==typeof e&&(this.loadingImage=b(e,this.props.crossOrigin).then(this.handleImageReady).catch(this.props.onLoadFailure))}},{key:"getInitialSize",value:function(e,t){var n,o,r=this.getDimensions();return t/e<r.height/r.width?o=e*((n=this.getDimensions().height)/t):n=t*((o=this.getDimensions().width)/e),{height:n,width:o}}},{key:"paintImage",value:function(e,t,n,o){var r,a=3<arguments.length&&void 0!==o?o:E;t.resource&&(r=this.calculatePosition(t,n),e.save(),e.translate(e.canvas.width/2,e.canvas.height/2),e.rotate(this.props.rotate*Math.PI/180),e.translate(-e.canvas.width/2,-e.canvas.height/2),this.isVertical()&&e.translate((e.canvas.width-e.canvas.height)/2,(e.canvas.height-e.canvas.width)/2),e.scale(a,a),e.globalCompositeOperation="destination-over",e.drawImage(t.resource,r.x,r.y,r.width,r.height),t.backgroundColor&&(e.fillStyle=t.backgroundColor,e.fillRect(r.x,r.y,r.width,r.height)),e.restore())}},{key:"calculatePosition",value:function(e,t){e=e||this.state.image;var n=g(this.getBorders(t),2),o=n[0],r=n[1],a=this.getCroppingRect(),i=e.width*this.props.scale,s=e.height*this.props.scale,u=-a.x*i,c=-a.y*s;return this.isVertical()?(u+=r,c+=o):(u+=o,c+=r),{x:u,y:c,height:s,width:i}}},{key:"paint",value:function(e){e.save(),e.scale(E,E),e.translate(0,0),e.fillStyle="rgba("+this.props.color.slice(0,4).join(",")+")";var t,n,o,r,a,i,s,u,c=this.props.borderRadius,l=this.getDimensions(),h=g(this.getBorders(l.border),2),d=h[0],f=h[1],p=l.canvas.height,v=l.canvas.width;c=Math.max(c,0),c=Math.min(c,v/2-d,p/2-f),e.beginPath(),t=e,r=v-2*(n=d),a=p-2*(o=f),0===(i=c)?t.rect(n,o,r,a):(s=r-i,u=a-i,t.translate(n,o),t.arc(i,i,i,Math.PI,1.5*Math.PI),t.lineTo(s,0),t.arc(s,i,i,1.5*Math.PI,2*Math.PI),t.lineTo(r,u),t.arc(s,u,i,2*Math.PI,.5*Math.PI),t.lineTo(i,a),t.arc(i,u,i,.5*Math.PI,Math.PI),t.translate(-n,-o)),e.rect(v,0,-v,p),e.fill("evenodd"),e.restore()}},{key:"render",value:function(){var e=this.props,t=(e.scale,e.rotate,e.image,e.border,e.borderRadius,e.width,e.height,e.position,e.color,e.backgroundColor,e.style),n=(e.crossOrigin,e.onLoadFailure,e.onLoadSuccess,e.onImageReady,e.onImageChange,e.onMouseUp,e.onMouseMove,e.onPositionChange,e.disableBoundaryChecks,e.disableHiDPIScaling,e.disableCanvasRotation,d(e,["scale","rotate","image","border","borderRadius","width","height","position","color","backgroundColor","style","crossOrigin","onLoadFailure","onLoadSuccess","onImageReady","onImageChange","onMouseUp","onMouseMove","onPositionChange","disableBoundaryChecks","disableHiDPIScaling","disableCanvasRotation"])),o=this.getDimensions(),a={width:o.canvas.width,height:o.canvas.height,cursor:this.state.drag?"grabbing":"grab",touchAction:"none"},i={width:o.canvas.width*E,height:o.canvas.height*E,style:c(c({},a),t)};return i[I.react.down]=this.handleMouseDown,w&&(i[I.react.mouseDown]=this.handleMouseDown),r.default.createElement("canvas",s({ref:this.setCanvas},i,n))}}])&&a(e.prototype,t),n&&a(e,n),u}();return i(C,"propTypes",{scale:o.default.number,rotate:o.default.number,image:o.default.oneOfType([o.default.string].concat(function(e){if(Array.isArray(e))return m(e)}(y=M?[o.default.instanceOf(File)]:[])||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(y)||v(y)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}())),border:o.default.oneOfType([o.default.number,o.default.arrayOf(o.default.number)]),borderRadius:o.default.number,width:o.default.number,height:o.default.number,position:o.default.shape({x:o.default.number,y:o.default.number}),color:o.default.arrayOf(o.default.number),backgroundColor:o.default.string,crossOrigin:o.default.oneOf(["","anonymous","use-credentials"]),onLoadFailure:o.default.func,onLoadSuccess:o.default.func,onImageReady:o.default.func,onImageChange:o.default.func,onMouseUp:o.default.func,onMouseMove:o.default.func,onPositionChange:o.default.func,disableBoundaryChecks:o.default.bool,disableHiDPIScaling:o.default.bool,disableCanvasRotation:o.default.bool}),i(C,"defaultProps",{scale:1,rotate:0,border:25,borderRadius:0,width:200,height:200,color:[0,0,0,.5],onLoadFailure:function(){},onLoadSuccess:function(){},onImageReady:function(){},onImageChange:function(){},onMouseUp:function(){},onMouseMove:function(){},onPositionChange:function(){},disableBoundaryChecks:!1,disableHiDPIScaling:!1,disableCanvasRotation:!0}),C}(n(45697),n(67294))},74488:function(e,t){"use strict";Object.defineProperty(t,"__esModule",{value:!0});t.ContentRect=function(e){if("getBBox"in e){var t=e.getBBox();return Object.freeze({height:t.height,left:0,top:0,width:t.width})}var n=window.getComputedStyle(e);return Object.freeze({height:parseFloat(n.height||"0"),left:parseFloat(n.paddingLeft||"0"),top:parseFloat(n.paddingTop||"0"),width:parseFloat(n.width||"0")})}},28981:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n(74488),r=function(){function e(e){this.target=e,this.$$broadcastWidth=this.$$broadcastHeight=0}return Object.defineProperty(e.prototype,"broadcastWidth",{get:function(){return this.$$broadcastWidth},enumerable:!0,configurable:!0}),Object.defineProperty(e.prototype,"broadcastHeight",{get:function(){return this.$$broadcastHeight},enumerable:!0,configurable:!0}),e.prototype.isActive=function(){var e=o.ContentRect(this.target);return!!e&&(e.width!==this.broadcastWidth||e.height!==this.broadcastHeight)},e}();t.ResizeObservation=r},30215:function(e,t,n){"use strict";var o=n(28981),r=n(32778),a=[],i=function(){function e(e){this.$$observationTargets=[],this.$$activeTargets=[],this.$$skippedTargets=[];var t=function(e){if("undefined"===typeof e)return"Failed to construct 'ResizeObserver': 1 argument required, but only 0 present.";if("function"!==typeof e)return"Failed to construct 'ResizeObserver': The callback provided as parameter 1 is not a function."}(e);if(t)throw TypeError(t);this.$$callback=e}return e.prototype.observe=function(e){var t,n=u("observe",e);if(n)throw TypeError(n);c(this.$$observationTargets,e)>=0||(this.$$observationTargets.push(new o.ResizeObservation(e)),t=this,a.indexOf(t)<0&&(a.push(t),g()))},e.prototype.unobserve=function(e){var t=u("unobserve",e);if(t)throw TypeError(t);var n=c(this.$$observationTargets,e);n<0||(this.$$observationTargets.splice(n,1),0===this.$$observationTargets.length&&s(this))},e.prototype.disconnect=function(){this.$$observationTargets=[],this.$$activeTargets=[],s(this)},e}();function s(e){var t=a.indexOf(e);t>=0&&(a.splice(t,1),m())}function u(e,t){return"undefined"===typeof t?"Failed to execute '"+e+"' on 'ResizeObserver': 1 argument required, but only 0 present.":t&&t.nodeType===window.Node.ELEMENT_NODE?void 0:"Failed to execute '"+e+"' on 'ResizeObserver': parameter 1 is not of type 'Element'."}function c(e,t){for(var n=0;n<e.length;n+=1)if(e[n].target===t)return n;return-1}t.do=i;var l,h=function(e){a.forEach((function(t){t.$$activeTargets=[],t.$$skippedTargets=[],t.$$observationTargets.forEach((function(n){n.isActive()&&(f(n.target)>e?t.$$activeTargets.push(n):t.$$skippedTargets.push(n))}))}))},d=function(){var e=1/0;return a.forEach((function(t){if(t.$$activeTargets.length){var n=[];t.$$activeTargets.forEach((function(t){var o=new r.ResizeObserverEntry(t.target);n.push(o),t.$$broadcastWidth=o.contentRect.width,t.$$broadcastHeight=o.contentRect.height;var a=f(t.target);a<e&&(e=a)})),t.$$callback(n,t),t.$$activeTargets=[]}})),e},f=function(e){for(var t=0;e.parentNode;)e=e.parentNode,t+=1;return t},p=function(){var e=0;for(h(e);a.some((function(e){return!!e.$$activeTargets.length}));)e=d(),h(e);a.some((function(e){return!!e.$$skippedTargets.length}))&&function(){var e=new window.ErrorEvent("ResizeLoopError",{message:"ResizeObserver loop completed with undelivered notifications."});window.dispatchEvent(e)}()},g=function(){l||v()},v=function(){l=window.requestAnimationFrame((function(){p(),v()}))},m=function(){l&&!a.some((function(e){return!!e.$$observationTargets.length}))&&(window.cancelAnimationFrame(l),l=void 0)}},32778:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n(74488),r=function(e){this.target=e,this.contentRect=o.ContentRect(e)};t.ResizeObserverEntry=r},66681:function(e,t,n){"use strict";n.d(t,{Pc:function(){return M},ck:function(){return k},fC:function(){return S}});var o=n(87462),r=n(67294),a=n(36206),i=n(65936),s=n(28771),u=n(25360),c=n(91276),l=n(75320),h=n(79698),d=n(77342),f=n(78990);const p="rovingFocusGroup.onEntryFocus",g={bubbles:!1,cancelable:!0},v="RovingFocusGroup",[m,b,y]=(0,i.B)(v),[w,M]=(0,u.b)(v,[y]),[O,I]=w(v),E=(0,r.forwardRef)(((e,t)=>(0,r.createElement)(m.Provider,{scope:e.__scopeRovingFocusGroup},(0,r.createElement)(m.Slot,{scope:e.__scopeRovingFocusGroup},(0,r.createElement)(T,(0,o.Z)({},e,{ref:t})))))),T=(0,r.forwardRef)(((e,t)=>{const{__scopeRovingFocusGroup:n,orientation:i,loop:u=!1,dir:c,currentTabStopId:v,defaultCurrentTabStopId:m,onCurrentTabStopIdChange:y,onEntryFocus:w,...M}=e,I=(0,r.useRef)(null),E=(0,s.e)(t,I),T=(0,f.gm)(c),[C=null,R]=(0,d.T)({prop:v,defaultProp:m,onChange:y}),[$,S]=(0,r.useState)(!1),k=(0,h.W)(w),x=b(n),D=(0,r.useRef)(!1),[F,j]=(0,r.useState)(0);return(0,r.useEffect)((()=>{const e=I.current;if(e)return e.addEventListener(p,k),()=>e.removeEventListener(p,k)}),[k]),(0,r.createElement)(O,{scope:n,orientation:i,dir:T,loop:u,currentTabStopId:C,onItemFocus:(0,r.useCallback)((e=>R(e)),[R]),onItemShiftTab:(0,r.useCallback)((()=>S(!0)),[]),onFocusableItemAdd:(0,r.useCallback)((()=>j((e=>e+1))),[]),onFocusableItemRemove:(0,r.useCallback)((()=>j((e=>e-1))),[])},(0,r.createElement)(l.WV.div,(0,o.Z)({tabIndex:$||0===F?-1:0,"data-orientation":i},M,{ref:E,style:{outline:"none",...e.style},onMouseDown:(0,a.M)(e.onMouseDown,(()=>{D.current=!0})),onFocus:(0,a.M)(e.onFocus,(e=>{const t=!D.current;if(e.target===e.currentTarget&&t&&!$){const t=new CustomEvent(p,g);if(e.currentTarget.dispatchEvent(t),!t.defaultPrevented){const e=x().filter((e=>e.focusable));P([e.find((e=>e.active)),e.find((e=>e.id===C)),...e].filter(Boolean).map((e=>e.ref.current)))}}D.current=!1})),onBlur:(0,a.M)(e.onBlur,(()=>S(!1)))})))})),C="RovingFocusGroupItem",R=(0,r.forwardRef)(((e,t)=>{const{__scopeRovingFocusGroup:n,focusable:i=!0,active:s=!1,tabStopId:u,...h}=e,d=(0,c.M)(),f=u||d,p=I(C,n),g=p.currentTabStopId===f,v=b(n),{onFocusableItemAdd:y,onFocusableItemRemove:w}=p;return(0,r.useEffect)((()=>{if(i)return y(),()=>w()}),[i,y,w]),(0,r.createElement)(m.ItemSlot,{scope:n,id:f,focusable:i,active:s},(0,r.createElement)(l.WV.span,(0,o.Z)({tabIndex:g?0:-1,"data-orientation":p.orientation},h,{ref:t,onMouseDown:(0,a.M)(e.onMouseDown,(e=>{i?p.onItemFocus(f):e.preventDefault()})),onFocus:(0,a.M)(e.onFocus,(()=>p.onItemFocus(f))),onKeyDown:(0,a.M)(e.onKeyDown,(e=>{if("Tab"===e.key&&e.shiftKey)return void p.onItemShiftTab();if(e.target!==e.currentTarget)return;const t=function(e,t,n){const o=function(e,t){return"rtl"!==t?e:"ArrowLeft"===e?"ArrowRight":"ArrowRight"===e?"ArrowLeft":e}(e.key,n);return"vertical"===t&&["ArrowLeft","ArrowRight"].includes(o)||"horizontal"===t&&["ArrowUp","ArrowDown"].includes(o)?void 0:$[o]}(e,p.orientation,p.dir);if(void 0!==t){e.preventDefault();let r=v().filter((e=>e.focusable)).map((e=>e.ref.current));if("last"===t)r.reverse();else if("prev"===t||"next"===t){"prev"===t&&r.reverse();const a=r.indexOf(e.currentTarget);r=p.loop?(o=a+1,(n=r).map(((e,t)=>n[(o+t)%n.length]))):r.slice(a+1)}setTimeout((()=>P(r)))}var n,o}))})))})),$={ArrowLeft:"prev",ArrowUp:"prev",ArrowRight:"next",ArrowDown:"next",PageUp:"first",Home:"first",PageDown:"last",End:"last"};function P(e){const t=document.activeElement;for(const n of e){if(n===t)return;if(n.focus(),document.activeElement!==t)return}}const S=E,k=R},60434:function(e,t,n){"use strict";n.d(t,{VY:function(){return k},aV:function(){return P},fC:function(){return $},xz:function(){return S}});var o=n(87462),r=n(67294),a=n(36206),i=n(25360),s=n(66681),u=n(29115),c=n(75320),l=n(78990),h=n(77342),d=n(91276);const f="Tabs",[p,g]=(0,i.b)(f,[s.Pc]),v=(0,s.Pc)(),[m,b]=p(f),y=(0,r.forwardRef)(((e,t)=>{const{__scopeTabs:n,value:a,onValueChange:i,defaultValue:s,orientation:u="horizontal",dir:f,activationMode:p="automatic",...g}=e,v=(0,l.gm)(f),[b,y]=(0,h.T)({prop:a,onChange:i,defaultProp:s});return(0,r.createElement)(m,{scope:n,baseId:(0,d.M)(),value:b,onValueChange:y,orientation:u,dir:v,activationMode:p},(0,r.createElement)(c.WV.div,(0,o.Z)({dir:v,"data-orientation":u},g,{ref:t})))})),w="TabsList",M=(0,r.forwardRef)(((e,t)=>{const{__scopeTabs:n,loop:a=!0,...i}=e,u=b(w,n),l=v(n);return(0,r.createElement)(s.fC,(0,o.Z)({asChild:!0},l,{orientation:u.orientation,dir:u.dir,loop:a}),(0,r.createElement)(c.WV.div,(0,o.Z)({role:"tablist","aria-orientation":u.orientation},i,{ref:t})))})),O="TabsTrigger",I=(0,r.forwardRef)(((e,t)=>{const{__scopeTabs:n,value:i,disabled:u=!1,...l}=e,h=b(O,n),d=v(n),f=C(h.baseId,i),p=R(h.baseId,i),g=i===h.value;return(0,r.createElement)(s.ck,(0,o.Z)({asChild:!0},d,{focusable:!u,active:g}),(0,r.createElement)(c.WV.button,(0,o.Z)({type:"button",role:"tab","aria-selected":g,"aria-controls":p,"data-state":g?"active":"inactive","data-disabled":u?"":void 0,disabled:u,id:f},l,{ref:t,onMouseDown:(0,a.M)(e.onMouseDown,(e=>{u||0!==e.button||!1!==e.ctrlKey?e.preventDefault():h.onValueChange(i)})),onKeyDown:(0,a.M)(e.onKeyDown,(e=>{[" ","Enter"].includes(e.key)&&h.onValueChange(i)})),onFocus:(0,a.M)(e.onFocus,(()=>{const e="manual"!==h.activationMode;g||u||!e||h.onValueChange(i)}))})))})),E="TabsContent",T=(0,r.forwardRef)(((e,t)=>{const{__scopeTabs:n,value:a,forceMount:i,children:s,...l}=e,h=b(E,n),d=C(h.baseId,a),f=R(h.baseId,a),p=a===h.value,g=(0,r.useRef)(p);return(0,r.useEffect)((()=>{const e=requestAnimationFrame((()=>g.current=!1));return()=>cancelAnimationFrame(e)}),[]),(0,r.createElement)(u.z,{present:i||p},(({present:n})=>(0,r.createElement)(c.WV.div,(0,o.Z)({"data-state":p?"active":"inactive","data-orientation":h.orientation,role:"tabpanel","aria-labelledby":d,hidden:!n,id:f,tabIndex:0},l,{ref:t,style:{...e.style,animationDuration:g.current?"0s":void 0}}),n&&s)))}));function C(e,t){return`${e}-trigger-${t}`}function R(e,t){return`${e}-content-${t}`}const $=y,P=M,S=I,k=T}}]);