<template>
  <main class="tnl-Layout_Main"  id="#app">
  	<div class="tnl-Breadcrumbs">
  		<span class="tnl-Breadcrumbs_Item">
  			   <router-link :to="{path:'/'}">Home</router-link>
  		    </span>
  		<span class="tnl-Breadcrumbs_Item">
  			   {{deporte.Nome}}
  		    </span>
  	</div>

  	<section class="stl-League">
  		<h1 class="tnl-AvatarHeroBlock_Title">Federacións de {{deporte.Nome}}</h1>
  		<section>
  		    <ul class="stl-MatchList" id="matchListApp">
  			    <div class="tnl-TableLeagueRound_Header">Seleccione unha Federación</div>
  			    <li class="stl-MatchList_Item" v-for="value in federaciones" v-bind:key="value.ID">
      				<div class="stl-MatchList_Data">
      		    	<p><router-link :to="{path:'/'+ deporte.ID + '/federacion/'+ value.Federacion_ID + '/competicion' }">{{value.Nome}}</router-link></p>
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
        federaciones: [],
        deporte:null
      }
    },
  mounted() {
    const URIFederacion = this.$URL +'/deporte/'+this.$route.params.id+'/federacion';
    const URIDeporte = this.$URL +'/deporte/'+this.$route.params.id;
    this.$http
      .get(URIFederacion)
      .then((result) => {this.federaciones = result.data})
      this.$http
        .get(URIDeporte)
        .then((result) => {this.deporte = result.data})
  }
  };
</script>
