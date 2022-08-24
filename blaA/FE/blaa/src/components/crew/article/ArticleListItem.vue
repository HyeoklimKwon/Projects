<template>
  <div class="article">
    <div class="row">
      <div class="col-2">
        <img class="imgProfile" :src="profile" />
      </div>
      <div class="col-10">
        <div class="row">
          <div class="col" style="padding: 0 0 0 25px">
            <div class="row mb-1" style="font-weight: bold">
              {{ nickname }}
            </div>
            <div class="row mb-1">
              {{ yyyyMMdd(created_at) }}
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div @click="moveToArticle(crew_article_pk)">
          <div v-if="images.length > 0">
            <img class="postImg" :src="host + images[0].article_picture" />
          </div>
          <div style="word-break: normal; font-size: 14px">
            {{ crew_content }}
          </div>
        </div>
      </div>
    </div>
  </div>

  <hr />

  <!-- <router-link :to="'/crew/article/detail/'+crew_article_pk">{{ crew_title }}</router-link> --->
  <!-- <router-link :to="{ name: 'articledetail', params: { crew_article_pk: crew_article_pk } }">{{ crew_title }}</router-link> -->
  <!-- {{ crew_title }} -->
</template>

<script>
import { dataChange } from "@/hooks/dateChange";
import { useRouter } from "vue-router";
import { ref } from "vue";
export default {
  props: {
    crew_article_pk: Number,
    crew: Number,
    crew_title: String,
    user: Number,
    created_at: String,
    crew_content: String,
    images: Array,
    crew_private: Boolean,
    crew_pin: Boolean,
    nickname: String,
    profile: String,
    updated_at: String,
    isMember: Boolean,
  },
  setup(props) {
    const { yyyyMMdd } = dataChange();

    const router = useRouter();
    const host = ref("https://i7b209.p.ssafy.io/");
    const create_date = ref("");
    const moveToArticle = (crew_article_pk) => {
      router.push({ name: "articledetail", params: { crew_article_pk: crew_article_pk } });
    };

    return {
      moveToArticle,
      host,
      yyyyMMdd,
    };
  },
};
</script>

<style scoped>
.imgProfile {
  width: 50px;
  height: 50px;
  border-radius: 70%;
  object-fit: cover;
  margin-top: 1px;
}
.article {
  width: 100%;
  padding: 30px;
  background-color: white;
}
.postImg {
  width: 250px;
  height: 250px;
  border-radius: 10%;
  object-fit: cover;
  margin-top: px;
  margin-bottom: 20px;
}
</style>
