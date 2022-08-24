<template>
  <thead>
    <th>순번</th>
    <th>제목</th>
    <th>내용</th>
    <th>작성자</th>
    <th>작성일자</th>
    <th>공개여부</th>
    <th>핀 고정</th>
  </thead>
  <tbody>
    <tr>
      <td>{{ crew_article_pk }}</td>
      <!-- <td>{{ crew }}</td> -->
      <td>
        <!-- <router-link :to="'/crew/article/detail/'+crew_article_pk">{{ crew_title }}</router-link> --->
        <router-link :to="{ name: 'articledetail', params: { crew_article_pk: crew_article_pk } }">{{ crew_title }}</router-link>
        <!-- {{ crew_title }} -->
      </td>
      <td>{{ crew_content }}</td>
      <td>{{ user }}</td>
      <td>{{ created_at }}</td>
      <td>{{ crew_private }}</td>
      <td>{{ crew_pin }}</td>
    </tr>
  </tbody>
</template>

<script>
export default {
  props: {
    crew_article_pk: Number,
    crew: Number,
    crew_title: String,
    user: Number,
    created_at: String,
    crew_content: String,
    crew_private: Boolean,
    crew_pin: Boolean,
  },
};
</script>

<style></style>
