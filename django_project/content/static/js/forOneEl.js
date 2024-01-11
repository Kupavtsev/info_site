window.addEventListener('DOMContentLoaded', function() {
    'use strict';

    let oneArticle = this.document.querySelector('.one_article')
    let articleDescription = this.document.querySelector('.article_description'),
        articleImage = this.document.querySelector('.article_img');
    let articlesBlock = this.document.querySelector('.Articles')
    let articleDescriptionsAll = this.document.querySelectorAll('.article_description')
    let articleImagesAll = this.document.querySelectorAll('.article_img')

    // My Version

    function showArticleDescription() {
        if (articleDescription.classList.contains('hide')) {
            articleImage.classList.add('hide');
            articleDescription.classList.remove('hide');
        }
    }
    function hideArticleDescription() {
        if (articleImage.classList.contains('hide')) {
            articleDescription.classList.add('hide');
            articleImage.classList.remove('hide');
        }
    }


    articleImage.addEventListener('mouseenter', function(event) {
        console.log(event.type)
        showArticleDescription();
    })
    articleDescription.addEventListener('mouseleave', function(event) {
        console.log(event.type)
        hideArticleDescription();
    })
})