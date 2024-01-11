window.addEventListener('DOMContentLoaded', function() {
    'use strict';

    let allArticles = this.document.querySelectorAll('.one_article');
    // let articlesBlock = this.document.querySelector('.Articles');
    let articlesBlock = this.document.querySelector('.description_hide');
    let articleDescriptionsAll = this.document.querySelectorAll('.article_description');
    let articleImagesAll = this.document.querySelectorAll('.article_img');



    function showArticleDescription(i) {
        if (articleDescriptionsAll[i].classList.contains('hide')) {
            articleImagesAll[i].classList.add('hide');
            articleDescriptionsAll[i].classList.remove('hide');
        }
    }
    function hideArticleDescription(i) {
        if (articleImagesAll[i].classList.contains('hide')) {
            articleDescriptionsAll[i].classList.add('hide');
            articleImagesAll[i].classList.remove('hide');
        }
    }




    articlesBlock.addEventListener('mouseover', function(event) {
        let target = event.target;
        if (target && target.classList.contains('article_img')) {
            for (let i=0; i < articleImagesAll.length; i++) {
                if (target == articleImagesAll[i]) {
                    showArticleDescription(i);

                    
                    allArticles[i].addEventListener('mouseleave', function(event) {
                        hideArticleDescription(i);
                    })
                }
            }
        }
    })
})