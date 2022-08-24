<template>
  <hr />
  <div>
    <button @click="business = true">업무용</button>
    <button @click="business = false">친목용</button>
    {{ business }}
  </div>

  <table>
    <thead>
      <tr>
        <th>순번</th>
        <th>크루명</th>
        <!-- <th>크루설명</th> -->
        <th>업무용/친목용</th>
        <th>크루장</th>
        <th>가입하기</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(crew, i) in filtered" :key="i" v-bind="crew">
        <td>{{ crew.crew_pk }}</td>
        <td>
          <router-link :to="{ name: 'crewboard', params: { crew_pk: crew.crew_pk } }">{{ crew.crew_name }}</router-link>
        </td>
        <td>{{ crew.crew_explain }}</td>
        <td>{{ crew.is_business }}</td>
        <td>{{ crew.crew_leader }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { useStore } from "vuex";
import { computed, reactive, ref } from "vue";
export default {
  setup() {
    const store = useStore();
    let AllCrews = reactive({
      crews: [],
    });
    const AllMembers = reactive({
      members: [],
    });
    let business = ref(true);

    const start = async () => {
      await store.dispatch("crew/allcrewlist");
      AllCrews.crews = store.state.crew.AllCrews.results;
    };
    const filtered = computed(() => {
      return AllCrews.crews.filter((item) => {
        return item.is_business === business.value;
      });
    });

    start();
    return {
      AllCrews,
      business,
      filtered,
    };
  },
};
</script>

<style></style>
