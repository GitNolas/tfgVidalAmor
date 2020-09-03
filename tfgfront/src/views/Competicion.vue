<template>
  <main class="tnl-Layout_Main"  id="#app">
  	<div class="tnl-Breadcrumbs">
  		<span class="tnl-Breadcrumbs_Item">
  			   <router-link :to="{path:'/'}">Home</router-link>
  		    </span>
  		<span class="tnl-Breadcrumbs_Item">
           <router-link :to="{path:'/'+ this.$route.params.id + '/federacion'}"> {{deporte.Nome}}</router-link>
  		    </span>
      <span class="tnl-Breadcrumbs_Item" v-for="value in federacion" v-bind:key="value.ID">
  			   {{value.Nome}}
  		    </span>
  	</div>

  	<section class="stl-League">
  		<h1 class="tnl-AvatarHeroBlock_Title" v-for="value in federacion" v-bind:key="value.ID">Competicións da {{value.Nome}}</h1>
  		<section>
  		    <ul class="stl-MatchList" id="matchListApp">
  			    <div class="tnl-TableLeagueRound_Header">Seleccione unha Competición</div>
  			    <li class="stl-MatchList_Item" v-for="value in competicions" v-bind:key="value.ID">
      				<div class="stl-MatchList_Data">
      		    	<p>
                  <router-link :to="{path:'/'+ deporte.ID +
                                          '/federacion/'+ $route.params.idfederacion+
                                          '/competicion/' + value.ID +
                                          '/resultados/'}">
                    {{value.Nome}}
                  </router-link>
                </p>
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
        federacion: null,
        deporte:null,
        competicions: []
      }
    },
  mounted() {
    const URIFederacion = this.$URL +'/federacion/'+this.$route.params.idfederacion;
    const URIDeporte = this.$URL +'/deporte/'+this.$route.params.id;
    const URICompeticion = this.$URL +'/federacion/'+this.$route.params.idfederacion+'/competicion';
    this.$http
      .get(URIFederacion)
      .then((result) => {this.federacion = result.data})
    this.$http
      .get(URIDeporte)
      .then((result) => {this.deporte = result.data})
    this.$http
      .get(URICompeticion)
      .then((result) => {this.competicions = result.data})
  }
  };
</script>
