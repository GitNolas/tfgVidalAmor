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
        <router-link :to="{path:'/'+ $route.params.id + '/federacion/'+ $route.params.idfederacion + '/competicion'}"> {{value.Nome}}</router-link>
      </span>
      <span class="tnl-Breadcrumbs_Item" >
        {{competicions.Nome}}
      </span>
    </div>

  	<section class="stl-League">
  		<h1 class="tnl-AvatarHeroBlock_Title">{{competicions.Nome}}</h1>
  		<section>
  		    <ul class="stl-MatchList" id="matchListApp" v-for="xornada in xornadas" v-bind:key="xornada.Xornada">
              <div class="tnl-TableLeagueRound_Header"> Xornada {{xornada.Xornada}}</div>
              <div v-for="value in resultados" v-bind:key="value.ID">
                <li class="stl-MatchList_Item" v-if="value.Xornada == xornada.Xornada">
                  <div class="stl-MatchList_Data" >
                    <p class="stl-MatchList_TeamName homeTeam">{{value.EquipoLocal}}</p>
                    <p class="stl-MatchList_ScoreBoard"><span>{{value.PtosLocal}} - {{value.PtosVisitante}}</span></p>
                    <p class="stl-MatchList_TeamName awayTeam">{{value.EquipoVisitante}}</p>
                  </div>
                  <div class="stl-MatchList_Data" >
                    <p class="stl-MatchList_TeamName homeTeam"><b>Data:</b> {{value.Data}}</p>
                    <p class="stl-MatchList_ScoreBoard"><span>{{value.Hora}}</span></p>
                    <p class="stl-MatchList_TeamName awayTeam"><b>Localización:</b> {{value.Localizacion}}</p>
                  </div>
                </li>
              </div>
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
        competicions: null,
        resultados: [],
        xornadas: []
      }
    },

  mounted() {
  const URIFederacion =this.$URL +'/federacion/'+this.$route.params.idfederacion;
  const URIDeporte = this.$URL +'/deporte/'+this.$route.params.id;
  const URICompeticion = this.$URL +'/competicion/'+this.$route.params.idcompeticion;
  const URIResultados = this.$URL +'/competicion/'+this.$route.params.idcompeticion +'/resultado';
  const URIXornadas = this.$URL +'/competicion/'+this.$route.params.idcompeticion+'/resultado/xornada';

  this.$http
    .get(URIFederacion)
    .then((result) => {this.federacion = result.data})
  this.$http
    .get(URIDeporte)
    .then((result) => {this.deporte = result.data})
  this.$http
    .get(URICompeticion)
    .then((result) => {this.competicions = result.data})
  this.$http
    .get(URIResultados)
    .then((result) => {this.resultados = result.data})
  this.$http
    .get(URIXornadas)
    .then((result) => {this.xornadas = result.data})
  }

  };
</script>
