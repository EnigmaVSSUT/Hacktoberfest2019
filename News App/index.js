//3ec4c0e860084d8eba84262ad086be8a

//grab the news container
let newsaccordion = document.getElementById('newsaccordion')
document.querySelector('body').style.background='#ffff99'
// document.querySelector('.card').style.color='green'

//create a get request
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=3ec4c0e860084d8eba84262ad086be8a', true);

xhr.onload = function () {
    if(this.status === 200){
        let json = JSON.parse(this.responseText)
        let articles = json.articles
        // console.log(articles)
        let newshtml = ""
        articles.forEach(function(element,index) {
            let news = `<div class="card">
                            <div class="card-header accordion-dark bg-dark" id="heading${index}">
                                <h5 class="mb-0">
                                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapse${index}" style="color:yellow;"
                                        aria-expanded="true" aria-controls="collapse${index}"> News ${index+1}:
                                        ${element["title"]}
                                    </button>
                                </h5>
                            </div>

                            <div id="collapse${index}" class="collapse" aria-labelledby="heading${index}" data-parent="#newsaccordion">
                                <div class="card-body"> ${element["content"]}.<a href="${element["url"]}" target="_blank"> Read More Here </a>  </div>
                            </div>
                        </div>`;
            newshtml+= news;
        });

        newsaccordion.innerHTML = newshtml
    }
    else{
        console.log("Some error occured")
    }
}

xhr.send()
