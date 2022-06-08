<template>
<div>  
  <div id="form-div">
  <form @submit.prevent="onSubmit" class="form" id="form1">
    <p class="name">
      <label for="title"></label>
      <input v-model="newArticle.title" name="name" type="text" class="validate[required,custom[onlyLetter],length[0,100]] feedback-input" placeholder="Title" id="title" />
    </p>      
    <p class="text">
      <label for="content"></label>
      <textarea  v-model="newArticle.content"  name="text"  type="text" class="validate[required,length[6,300]] feedback-input" id="content" placeholder="Content"></textarea>
    </p>
    
    <div class="submit">
      <input type="submit" value="Confirm" id="button-blue"/>
      <div class="ease"></div>
    </div>
  </form>
</div>
</div>

  
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Montserrat:400,700);

html{
  height:100%;
}

#form-div {
  background-color: rgba(93, 93, 93, 0.4);
  padding:35px 35px 50px;
  width: 450px;
  left: 50%;
  position: absolute;
  margin-top:30px;
  margin-left: -260px;
  -moz-border-radius: 7px;
  -webkit-border-radius: 7px;
}

.feedback-input {
  color:#3c3c3c;
  font-family: Helvetica, Arial, sans-serif;
  font-weight:500;
  font-size: 18px;
  border-radius: 0;
  line-height: 22px;
  background-color: #ffffff;
  padding: 13px 13px 13px 54px;
  margin-bottom: 10px;
  width:100%;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
  border: 3px solid rgba(0,0,0,0);
}

.feedback-input:focus{
  background: #fff;
  box-shadow: 0;
  /*border: 3px solid #3498db;*/
  border-color: #3498db;
  color: #3498db;
  outline: none;
  /*padding: 13px 13px 13px 54px;*/
}

.focused {
  color:#30aed6;
  border:#30aed6 solid 3px;
}

/* Icons */
#name{
  background-image: url(http://rexkirby.com/kirbyandson/images/name.svg);
  background-size: 30px 30px;
  background-position: 11px 8px;
  background-repeat: no-repeat;
}

#email{
  background-image: url(http://rexkirby.com/kirbyandson/images/email.svg);
  background-size: 30px 30px;
  background-position: 11px 8px;
  background-repeat: no-repeat;
}

#comment{
  background-image: url(http://rexkirby.com/kirbyandson/images/comment.svg);
  background-size: 30px 30px;
  background-position: 11px 8px;
  background-repeat: no-repeat;
}

textarea {
  width: 100%;
  height: 150px;
  line-height: 150%;
  resize:vertical;
}

input:hover, textarea:hover,
input:focus, textarea:focus {
  background-color:white;
}

#button-blue{
  font-family: 'Montserrat', Arial, Helvetica, sans-serif;
  float:left; /* 플롯 중요(::after 가상요소 이용)*/
  width: 100%;
  border: #fbfbfb solid 4px;
  cursor:pointer;
  background-color: #3498db;
  color:white;
  font-size:24px;
  padding-top:22px;
  padding-bottom:22px;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
  margin-top:-4px;
  font-weight:700;
}

#button-blue:hover{
  background-color: rgba(0,0,0,0);
  color: #0493bd;
}

.ease {
  width: 0;
  height: 74px;
  background-color: #fbfbfb;
  -webkit-transition: .3s ease;
  -moz-transition: .3s ease;
  -o-transition: .3s ease;
  -ms-transition: .3s ease;
  transition: .3s ease;
}

.submit:hover .ease{
  width:100%;
  background-color:white;
}</style>

