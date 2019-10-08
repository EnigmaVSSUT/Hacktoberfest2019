function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function scroller() {
    var divTag = document.getElementsByClassName('isgrP');
    var d = divTag[0];
    var oldHeight = d.scrollTop;
    var newHeight = 0;
    while (true){
        newHeight += oldHeight + 500;
        await sleep(500);
        d.scrollTo(0, newHeight);
        if (oldHeight === d.scrollHeight){
            break;
        }
        oldHeight = d.scrollHeight;
    }
}
