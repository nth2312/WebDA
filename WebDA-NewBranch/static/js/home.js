
var htmlDiv = document.getElementById("rs-plugin-settings-inline-css"); var htmlDivCss = ".tp-caption.large_text,.large_text{color:#fff;font-weight:700;font-size:40px;line-height:40px;font-family:Arial;border-width:0px;border-style:none;position:absolute;text-shadow:0px 2px 5px rgba(0,0,0,0.5);white-space:nowrap}.tp-caption.News-Title,.News-Title{color:rgba(255,255,255,1.00);font-size:70px;line-height:60px;font-weight:400;font-style:normal;font-family:Roboto Slab;text-decoration:none;background-color:transparent;border-color:transparent;border-style:none;border-width:0px;border-radius:0px 0px 0px 0px}";
if (htmlDiv) {
    htmlDiv.innerHTML = htmlDiv.innerHTML + htmlDivCss;
} else {
    var htmlDiv = document.createElement("div");
    htmlDiv.innerHTML = "<style>" + htmlDivCss + "</style>";
    document.getElementsByTagName("head")[0].appendChild(htmlDiv.childNodes[0]);
}