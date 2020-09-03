<template>
  <div id="app">
  <a href="https://www.siguetuliga.com/"><img src="../public/siguetuliga.png" alt="Italian Trulli" ></a>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
    <a href="https://www.usc.gal/gl"><img src="../public/USC.png" alt="Italian Trulli" ></a>
    <a href="https://www.usc.gal/etse/"><img src="../public/etse.png" alt="Italian Trulli" ></a>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.stl-Match {
  min-width: 320px;
  max-width: 480px;
  margin: 0 auto 2em;
  background: $white;
}

.stl-MatchList {
    list-style: none;
    padding: 0;
    margin: 0;
}

.stl-MatchList_Item {
    position: relative;
    border-bottom: 1px solid #ddd;
}

.stl-MatchList_Data {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.stl-MatchList_TeamName {
  flex: 1;
  margin: .5em 0;
}

.awayTeam {
	text-align: left;
}

.homeTeam {
	text-align: right;
}

.stl-MatchList_ScoreBoard {
    min-width: 45px;
    max-width: 60px;
    padding: 0 .5em;
    border-right: 1px solid #ddd;
    border-left: 1px solid #ddd;
    margin: 1em;
    text-align: center;
    font-weight: 700;
}

.stl-MatchList_Link {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.tnl-Button-cta {
    overflow: hidden;
    position: relative;
    box-sizing: border-box;
    cursor: pointer;
    user-select: none;
    display: inline-block;
    border: 1px solid transparent;
    border-radius: 2px;
    font-family: Roboto,Helvetica,Arial,sans-serif;
    font-weight: 700;
    text-align: center;
    text-decoration: none;
    white-space: nowrap;
    transition: .2s ease-out;
    font-size: .938em;
    height: 36px;
    line-height: 35px;
    padding: 0 .8rem;
    background-color: #e31c79;
    color: #fff;
}
.tnl-TableLeagueRound_Header {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-pack: distribute;
    justify-content: space-around;
    padding: .5em 0;
    background: #333;
    color: #fff;
}
.stl-League {
    background: #fff;
    position: relative;
}
article, aside, figcaption, figure, footer, header, main, section {
    display: block;
}
.tnl-AvatarHeroBlock_Title {
    padding-top: 1.5em;
    margin-bottom: .5em;
    text-align: center;
}
@media only screen and (min-width: 56.25em) {
	.stl-League {
	    max-width: 66.47399%;
	    margin: 0 auto;
	}
	.tnl-Layout_Main {
	    min-width: 900px;
	    max-width: 1044px;
	    padding: 0 1em;
	}
	.tnl-Breadcrumbs {
	    max-width: 66.47399%;
	    margin: 0 auto;
	}
}
body {
    background: #f4f4f4;
    font-size: 16px;
    line-height: 1.3;
}
.tnl-Breadcrumbs {
    overflow-y: auto;
    width: 100%;
    padding: 1em 0;
    background: #333;
    font-size: .875rem;
    white-space: nowrap;
}
.tnl-Breadcrumbs_Item:not(:last-child) {
    color: #999;
}
.tnl-Breadcrumbs_Item:not(:last-child) a {
    color: #999;
}
.tnl-Breadcrumbs_Item:first-child {
    margin-left: 1em;
}
.tnl-Breadcrumbs_Item:not(:last-child):after {
    content: "\276F";
    margin-left: .3em;
}
.tnl-Breadcrumbs_Item:last-child {
    margin-right: 1em;
    color: #fff;
    font-weight: 700;
}
.tnl-Layout_Main {
    margin: auto;
}
</style>
