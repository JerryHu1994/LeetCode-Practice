"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[280],{98628:function(e,t,a){function i(e){if(null===e||void 0===e?void 0:e.startsWith("http")){var t=new URL(e);return t.searchParams.set("x-oss-process","image/format,webp"),t.toString()}return"".concat(e,"?x-oss-process=image/format,webp")}a.d(t,{s:function(){return i}})},84945:function(e,t,a){a.d(t,{y:function(){return l}});var i=a(29815),c=a(85893),n=(a(67294),a(20745)),V=a(51295),X=a(42437),o=a(6905),d=function(e){return(0,V.yI)("fixed bottom-0 left-0 right-0 pointer-events-none z-message",e)},_=function(e){var t=document.getElementById("messages-provider");if(!t){var a=document.createElement("div");a.id="messages-provider",document.body.appendChild(a),t=a,window.addEventListener("scroll",(function(){t&&(t.className=d(e))}))}return t.className=d(e),t.style.top=function(){var e=54+(0,i.Z)(document.getElementsByClassName(X.l)).reduce((function(e,t){return e+t.clientHeight}),0);return window.innerWidth<680?54:window.scrollY<=e?e-window.scrollY:4}()+"px",t},r=function(e,t){var a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:.5,i=arguments.length>3?arguments[3]:void 0,V=arguments.length>4?arguments[4]:void 0,X=arguments.length>5?arguments[5]:void 0,d=_(V||""),r=document.createElement("div");r.className="transition-opacity duration-500 ease-in-out z-message",d.appendChild(r);var l,u=(0,n.createRoot)(r),s=-1,O=function(e){s=window.setTimeout((function(){r.className+=" opacity-0",l&&l(i&&i()),setTimeout((function(){u.unmount(),r.remove()}),500)}),e)},k=function(e){-1!==s&&(clearTimeout(s),e||O(1e3*a))};return u.render((0,c.jsx)(o.Z,{content:t,type:e,onEnter:function(){return k(!0)},onLeave:function(){return k(!1)},className:X})),new Promise((function(e){l=e,O(1e3*a)}))},l={info:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("info",e,i,c,n,V)},warn:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("warning",e,i,c,n,V)},warning:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("warning",e,i,c,n,V)},success:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("success",e,i,c,n,V)},error:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("error",e,i,c,n,V)},plain:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=t.duration,i=void 0===a?2:a,c=t.onClose,n=t.containerClassName,V=t.itemClassName;return r("plain",e,i,c,n,V)}}},6905:function(e,t,a){var i=a(85893),c=(a(67294),a(84539)),n=a(51295),V=a(67021),X=a(86639),o=a(1452),d=a(15371);t.Z=function(e){var t=e.className,a=e.content,_=e.type,r=e.onEnter,l=void 0===r?function(){return null}:r,u=e.onLeave,s=void 0===u?function(){return null}:u,O={info:(0,i.jsx)(V.e,{width:"18px",height:"18px",className:"mr-2 fill-blue-s dark:fill-dark-blue-s"}),error:(0,i.jsx)(X.X,{width:"18px",height:"18px",className:"mr-2 fill-red-s dark:fill-dark-red-s"}),warning:(0,i.jsx)(V.e,{width:"18px",height:"18px",className:"mr-2 fill-yellow dark:fill-dark-yellow"}),success:(0,i.jsx)(o.A,{width:"18px",height:"18px",className:"mr-2 fill-green-s dark:fill-dark-green-s"}),plain:(0,i.jsx)(i.Fragment,{})};return(0,i.jsx)(c.u,{appear:!0,show:!0,enter:"transition duration-500 ease-out",enterFrom:"transform scale-95 opacity-0",enterTo:"transform scale-100 opacity-100",leave:"transition duration-500 ease-out",leaveFrom:"transform scale-100 opacity-100",leaveTo:"transform scale-95 opacity-0",children:(0,i.jsx)("div",{className:"flex justify-center",children:(0,i.jsxs)("div",{className:(0,n.yI)("px-4 py-1.5",d.Cj.bgPaper,d.Cj.label1,d.eq.commandBar,"pointer-events-auto my-2 flex items-center rounded-full",t),onMouseEnter:l,onMouseLeave:s,children:[O[_]," ",(0,i.jsx)("span",{children:a})]})})})}},42437:function(e,t,a){a.d(t,{l:function(){return i}});var i="announcement-bar__container"},73986:function(e,t,a){a.d(t,{y:function(){return l}});var i=a(26042),c=a(69396),n=a(99534),V=a(85893),X=a(67294),o=a(75117),d=a(98628),_=a(82670);var r=X.forwardRef((function(e,t){var a=e.src,r=e.errPlaceholder,l=e.children,u=(0,n.Z)(e,["src","errPlaceholder","children"]),s=a&&function(e){return e.startsWith("http")||o.Oo?e:0}(a),O=(0,X.useState)(s),k=(O[0],O[1]),C=(0,X.useCallback)((function(){r&&k(r)}),[r,k]),E=function(e,t){var a=(0,X.useRef)(null),i=(0,X.useState)(!1),c=i[0],n=i[1],V=(0,X.useCallback)((function(a){c||((0,_.Z)(a.target,HTMLSourceElement)?a.target.srcset=e:a.target.src=e,n(!0),null===t||void 0===t||t())}),[e,c,t]);return(0,X.useEffect)((function(){if(a&&a.current){var i=a.current,c=i.complete,n=i.naturalHeight;c&&0===n&&((0,_.Z)(a.current,HTMLSourceElement)?a.current.srcset=e:a.current.src=e,null===t||void 0===t||t())}}),[e,t]),e?{ref:a,onError:V}:{}}(r?(0,d.s)(r):"",C);(0,X.useEffect)((function(){k(s)}),[s]);null===a||void 0===a||a.toLowerCase().endsWith("svg");return(0,V.jsx)("img",(0,c.Z)((0,i.Z)({src:a,ref:t},E,u),{children:l}))}));r.displayName="LcImg";var l=r},1452:function(e,t,a){a.d(t,{A:function(){return V}});var i=a(26042),c=a(69396),n=a(85893),V=a(67294).forwardRef((function(e,t){return(0,n.jsx)("svg",(0,c.Z)((0,i.Z)({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",width:"1em",height:"1em",fill:"currentColor",ref:t},e),{children:(0,n.jsx)("path",{fillRule:"evenodd",d:"M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm-1.219-8.94l-1.805-1.804a1 1 0 00-1.414 1.414l2.512 2.512a1 1 0 001.414 0l4.95-4.95a1 1 0 10-1.414-1.414l-4.243 4.243z",clipRule:"evenodd"})}))}))},86639:function(e,t,a){a.d(t,{X:function(){return V}});var i=a(26042),c=a(69396),n=a(85893),V=a(67294).forwardRef((function(e,t){return(0,n.jsx)("svg",(0,c.Z)((0,i.Z)({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",width:"1em",height:"1em",fill:"currentColor",ref:t},e),{children:(0,n.jsx)("path",{fillRule:"evenodd",d:"M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm1.414-10l2.293-2.293a1 1 0 00-1.414-1.414L12 10.586 9.707 8.293a1 1 0 00-1.414 1.414L10.586 12l-2.293 2.293a1 1 0 101.414 1.414L12 13.414l2.293 2.293a1 1 0 001.414-1.414L13.414 12z",clipRule:"evenodd"})}))}))},67021:function(e,t,a){a.d(t,{e:function(){return V}});var i=a(26042),c=a(69396),n=a(85893),V=a(67294).forwardRef((function(e,t){return(0,n.jsx)("svg",(0,c.Z)((0,i.Z)({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",width:"1em",height:"1em",fill:"currentColor",ref:t},e),{children:(0,n.jsx)("path",{fillRule:"evenodd",d:"M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-11a1 1 0 00-1 1v4a1 1 0 102 0v-4a1 1 0 00-1-1zm0-3a1 1 0 100 2 1 1 0 000-2z",clipRule:"evenodd"})}))}))},29297:function(e,t,a){a.d(t,{d:function(){return n}});var i=a(33802),c=a(23025),n={qdNewEditorExposure:function(){var e={key:"qd_new_editor_exposure",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdOldEditorExposure:function(){var e={key:"qd_old_editor_exposure",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNewEditorMenuClick:function(e){var t={key:"qd_new_editor_menu_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdNewEditorVersionClick:function(e){var t={key:"qd_new_editor_version_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRichtextContentPublishRateExposure:function(e){var t={key:"qd_richtext_content_publish_rate_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPageExposure:function(e){var t={key:"qd_page_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdListClick:function(e){var t={key:"qd_list_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPrevQuestionClick:function(e){var t={key:"qd_prev_question_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdNextQuestionClick:function(e){var t={key:"qd_next_question_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRandomQuestionClick:function(e){var t={key:"qd_random_question_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdOpenPanelClick:function(e){var t={key:"qd_qd_open_panel_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDrawerQuestionClick:function(e){var t={key:"qd_drawer_question_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdShowTagsClick:function(e){var t={key:"qd_show_tags_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdShowTimeClick:function(e){var t={key:"qd_show_time_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdHideTimeClick:function(e){var t={key:"qd_hide_time_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdResetTimeClick:function(e){var t={key:"qd_reset_time_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchOldClick:function(){var e={key:"qd_switch_old_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdSwitchTabClick:function(e){var t={key:"qd_switch_tab_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDescHintsClick:function(e){var t={key:"qd_desc_hints_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDescHintsSwitchClick:function(e){var t={key:"qd_desc_hints_switch_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDescHintsContentExposure:function(e){var t={key:"qd_desc_hints_content_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQuestionVoteClick:function(e){var t={key:"qd_question_vote_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchPageLangClick:function(e){var t={key:"qd_switch_page_lang_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAddToListClick:function(e){var t={key:"qd_add_to_list_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCompanyPageExposure:function(e){var t={key:"qd_company_page_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCompanyPopupExposure:function(e){var t={key:"qd_company_popup_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCompanyIconClick:function(e){var t={key:"qd_company_icon_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdShareQuestionClick:function(e){var t={key:"qd_share_question_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdKeywordExposure:function(e){var t={key:"qd_keyword_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAnswerSeenInInterviewClick:function(e){var t={key:"qd_answer_seen_in_interview_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAnswerCompanyClick:function(e){var t={key:"qd_answer_company_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAnswerEncounterClick:function(e){var t={key:"qd_answer_encounter_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAnswerStageClick:function(e){var t={key:"qd_answer_stage_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSurveyCompleteExposure:function(e){var t={key:"qd_survey_complete_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRelatedTopicsClick:function(e){var t={key:"qd_related_topics_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRelatedCompaniesClick:function(e){var t={key:"qd_related_companies_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchLangClick:function(e){var t={key:"qd_switch_lang_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdFormatCodeClick:function(e){var t={key:"qd_format_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdEnableLspClick:function(e){var t={key:"qd_enable_lsp_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDisableLspClick:function(e){var t={key:"qd_disable_lsp_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdLspButtonClick:function(e){var t={key:"qd_lsp_button_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdEditorToolbarClick:function(e){var t={key:"qd_editor_toolbar_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdResetCodeConfirmClick:function(e){var t={key:"qd_reset_code_confirm_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdInsertFlagCodeClick:function(e){var t={key:"qd_insert_flag_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdConsoleExposure:function(e){var t={key:"qd_console_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchTestcaseModeClick:function(e){var t={key:"qd_switch_testcase_mode_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPopoverTestcaseModeClick:function(e){var t={key:"qd_popover_testcase_mode_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchConsolePosClick:function(e){var t={key:"qd_switch_console_pos_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAddCaseTabClick:function(e){var t={key:"qd_add_case_tab_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRemoveCaseTabClick:function(e){var t={key:"qd_remove_case_tab_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCreateCaseHintClick:function(e){var t={key:"qd_create_case_hint_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdVisualizationBtnExposure:function(e){var t={key:"qd_visualization_btn_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdVisualizerBtnClick:function(e){var t={key:"qd_visualizer_btn_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCheckAllTreeClick:function(e){var t={key:"qd_check_all_tree_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCaseTagClick:function(e){var t={key:"qd_case_tag_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCaseTagExposure:function(e){var t={key:"qd_case_tag_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdResultInfoClick:function(e){var t={key:"qd_result_info_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDiffBtnClick:function(e){var t={key:"qd_diff_btn_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdConsoleBtnClick:function(e){var t={key:"qd_console_btn_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdResetTestcasesClick:function(e){var t={key:"qd_reset_testcases_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubmitCodeClick:function(e){var t={key:"qd_submit_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRunCodeClick:function(e){var t={key:"qd_run_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQuickTestClick:function(e){var t={key:"qd_quick_test_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQuickDebugClick:function(e){var t={key:"qd_quick_debug_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdEnterDebugModeClick:function(e){var t={key:"qd_enter_debug_mode_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdStartDebugClick:function(e){var t={key:"qd_start_debug_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdStopDebugClick:function(e){var t={key:"qd_stop_debug_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdExitDebugClick:function(e){var t={key:"qd_exit_debug_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAddWatchExpClick:function(e){var t={key:"qd_add_watch_exp_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdRmWatchExpClick:function(e){var t={key:"qd_rm_watch_exp_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDebugControlsClick:function(e){var t={key:"qd_debug_controls_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionSearchClick:function(e){var t={key:"qd_solution_search_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdResetSearchTagsClick:function(e){var t={key:"qd_reset_search_tags_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSortSolutionClick:function(e){var t={key:"qd_sort_solution_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionItemExposure:function(e){var t={key:"qd_solution_item_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionItemClick:function(e){var t={key:"qd_solution_item_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdEnterAuthorProfileClick:function(e){var t={key:"qd_enter_author_profile_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdLeavePostClick:function(e){var t={key:"qd_leave_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdEditPostClick:function(e){var t={key:"qd_edit_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdUpVotePostClick:function(e){var t={key:"qd_up_vote_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDownVotePostClick:function(e){var t={key:"qd_down_vote_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdFavoritePostClick:function(e){var t={key:"qd_favorite_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdViewPostCommentClick:function(e){var t={key:"qd_view_post_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSharePostClick:function(e){var t={key:"qd_share_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubscribePostCnClick:function(e){var t={key:"qd_subscribe_post_cn_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubscribePostClick:function(e){var t={key:"qd_subscribe_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPrevNextPostClick:function(e){var t={key:"qd_prev_next_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionPaginationClick:function(e){var t={key:"qd_solution_pagination_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionDetailExposure:function(e){var t={key:"qd_solution_detail_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSolutionSideSwitchClick:function(e){var t={key:"qd_solution_side_switch_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPublishPostClick:function(e){var t={key:"qd_publish_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdCancelPostEditClick:function(e){var t={key:"qd_cancel_post_edit_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdUpdatePostClick:function(e){var t={key:"qd_update_post_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdMarkdownGuideClick:function(e){var t={key:"qd_markdown_guide_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdOverwriteWithLatestAcClick:function(e){var t={key:"qd_overwrite_with_latest_ac_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSortCommentClick:function(e){var t={key:"qd_sort_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPreviewCommentClick:function(e){var t={key:"qd_preview_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubmitCommentClick:function(e){var t={key:"qd_submit_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdUpVoteCommentClick:function(e){var t={key:"qd_up_vote_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDownVoteCommentClick:function(e){var t={key:"qd_down_vote_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdShareCommentClick:function(e){var t={key:"qd_share_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdReplyCommentClick:function(e){var t={key:"qd_reply_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdExpandCommentClick:function(e){var t={key:"qd_expand_comment_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdShowRepliesClick:function(e){var t={key:"qd_show_replies_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdHideRepliesClick:function(e){var t={key:"qd_hide_replies_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdStatusFilterClick:function(e){var t={key:"qd_status_filter_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdLangFilterClick:function(e){var t={key:"qd_lang_filter_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubmissionListClick:function(e){var t={key:"qd_submission_list_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAddNoteClick:function(e){var t={key:"qd_add_note_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubmissionCloseClick:function(){var e={key:"qd_submission_close_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNextChallengeClick:function(e){var t={key:"qd_next_challenge_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdMoreChallengeClick:function(e){var t={key:"qd_more_challenge_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSubmissionViewDetailClick:function(e){var t={key:"qd_submission_view_detail_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPostSolutionClick:function(e){var t={key:"qd_post_solution_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPostSolutionExposure:function(e){var t={key:"qd_post_solution_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdDistributionExposure:function(e){var t={key:"qd_distribution_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdViewSampleCodeClick:function(e){var t={key:"qd_view_sample_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdSwitchSampleCodeClick:function(e){var t={key:"qd_switch_sample_code_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAcceptDetailsClick:function(e){var t={key:"qd_accept_details_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdComplexityPopupExposure:function(e){var t={key:"qd_complexity_popup_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdComplexityPopupVoteClick:function(e){var t={key:"qd_complexity_popup_vote_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdComplexityPopupNotAccuracyClick:function(){var e={key:"qd_complexity_popup_not_accuracy_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdFeatureGuideExposure:function(e){var t={key:"qd_feature_guide_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdFinishDailyChallengeExposure:function(e){var t={key:"qd_finish_daily_challenge_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdMakeUpChallengeExposure:function(e){var t={key:"qd_make_up_challenge_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdIdeExpModalExposure:function(){var e={key:"qd_ide_exp_modal_exposure",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdIdeExpModalCancelClick:function(){var e={key:"qd_ide_exp_modal_cancel_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdIdeExpModalConfirmClick:function(){var e={key:"qd_ide_exp_modal_confirm_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNavbarOpenIdeClick:function(){var e={key:"qd_navbar_open_ide_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdSettingBackQdClick:function(){var e={key:"qd_setting_back_qd_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdDragChangeLayoutClick:function(e){var t={key:"qd_drag_change_layout_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAiToggleButtonClick:function(e){var t={key:"qd_ai_toggle_button_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAiCodeResponseExposure:function(e){var t={key:"qd_ai_code_response_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAiPremiumModalExposure:function(e){var t={key:"qd_ai_premium_modal_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAiPremiumSubscribeClick:function(e){var t={key:"qd_ai_premium_subscribe_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdAiHintSuccessExposure:function(e){var t={key:"qd_ai_hint_success_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPremiumCloudSavingRestoredClick:function(e){var t={key:"qd_premium_cloud_saving_restored_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPremiumUpgradeCloudSavingClick:function(e){var t={key:"qd_premium_upgrade_cloud_saving_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdPremiumCloudSavingToastClick:function(e){var t={key:"qd_premium_cloud_saving_toast_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdUpgradeToDynamicLayoutExposure:function(){var e={key:"qd_qd_upgrade_to_dynamic_layout_exposure",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdQdUpgradeToDynamicLayoutTryClick:function(){var e={key:"qd_qd_upgrade_to_dynamic_layout_try_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdQdLivePreviewExposure:function(e){var t={key:"qd_qd_live_preview_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdLivePreviewRefreshClick:function(e){var t={key:"qd_qd_live_preview_refresh_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdLivePreviewOpenNewTabClick:function(e){var t={key:"qd_qd_live_preview_open_new_tab_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdWebConsoleExposure:function(e){var t={key:"qd_qd_web_console_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdWebConsoleClearClick:function(e){var t={key:"qd_qd_web_console_clear_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdWebConsoleInputClick:function(e){var t={key:"qd_qd_web_console_input_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdFrameworkSwitcherExposure:function(e){var t={key:"qd_qd_framework_switcher_exposure",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdFrameworkSwitcherClickClick:function(e){var t={key:"qd_qd_framework_switcher_click_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdQdFrameworkSwitcherCloseClick:function(e){var t={key:"qd_qd_framework_switcher_close_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdNavbarLogoClick:function(e){var t={key:"qd_navbar_logo_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)},qdNavbarOpenNewTabClick:function(){var e={key:"qd_navbar_open_new_tab_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNavbarTimerStartClick:function(){var e={key:"qd_navbar_timer_start_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNavbarTimerEndClick:function(){var e={key:"qd_navbar_timer_end_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdNavbarUserDropdownClick:function(){var e={key:"qd_navbar_user_dropdown_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdDetailCodeToEditorClick:function(){var e={key:"qd_detail_code_to_editor_click",data:{}};i.V[c.X.GIO](e),i.V[c.X.GA4](e),i.V[c.X.CONSOLE](e),i.V[c.X.SELF_DB](e),i.V[c.X.DW](e)},qdContestSwitchToClassicClick:function(e){var t={key:"qd_contest_switch_to_classic_click",data:e};i.V[c.X.GIO](t),i.V[c.X.GA4](t),i.V[c.X.CONSOLE](t),i.V[c.X.SELF_DB](t),i.V[c.X.DW](t)}}}}]);