window.addEventListener('DOMContentLoaded', function() {
    'use strict';

    let allArticles = this.document.querySelectorAll('.one_article')
    let oneArticle = this.document.querySelector('.one_article')
    let oneArticleA = this.document.querySelector('.one_article a')
    let articleDescription = this.document.querySelector('.article_description'),
        articleImage = this.document.querySelector('.article_img');
    let articlesBlock = this.document.querySelector('.Articles')
    let articleDescriptionsAll = this.document.querySelectorAll('.article_description')
    let articleImagesAll = this.document.querySelectorAll('.article_img')



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
                    // articleDescriptionsAll[i].addEventListener('mouseleave', function(event) {
                    // articlesBlock.addEventListener('mouseleave', function(event) {
                        let target = event.target;
                        console.log(event.type);
                        console.log('TARGET: ', target);
                        hideArticleDescription(i);
                    })
                }
            }
        }
    })
})