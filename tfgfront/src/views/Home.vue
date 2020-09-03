
<template>
  <main class="tnl-Layout_Main"  id="#app">
  	<section class="stl-League">
  		<h1 class="tnl-AvatarHeroBlock_Title">Deportes</h1>
  		<section>
  		    <ul class="stl-MatchList" id="matchListApp">
  			    <div class="tnl-TableLeagueRound_Header">Seleccione un deporte</div>
  			    <li class="stl-MatchList_Item" v-for="value in deportes" v-bind:key="value.ID">
      				<div class="stl-MatchList_Data">
                <p><router-link :to="{path:'/'+ value.ID + '/federacion'}">{{value.Nome}}</router-link></p>

      				</div>
  			    </li>
  		    </ul>
  		</section>
  	</section>
  </main>
</template>
<script>
  export default {
    name: '#app',
    data () {
      return {
        deportes: []
      }
    },
  mounted() {
    const URIDeportes = this.$URL +'/deporte';
    this.$http
      .get(URIDeportes)
      .then((result) => {this.deportes = result.data})
  }
  };
</script>
