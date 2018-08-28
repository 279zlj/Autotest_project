<template>
  <div id="app">
    <div class="hello container-fluid">
      <div class="row container-fluid">
        <div class="col-lg-3 col-md-2 col-sm-2 col-xs-2">
          <router-view />
        </div>
        <div class="col-lg-9 col-md-9 col-sm-8 col-xs-9">
          <keep-alive>
            <router-view name="right"></router-view>
          </keep-alive>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  provide(){
    return{
      reload:this.reload
    }
  },
  methods:{
    reload(){
      this.isRouterAlive=false
      this.$nextTick(function () {
        this.isRouterAlive=true
      })
    }
  }
}
</script>

<style>
  body,html{
    height: 100%;
    margin: 0;
    padding: 0;

  }
  ::-webkit-scrollbar{display: none}
  #app{
    height: 100%;
    position:absolute;
    z-index: 999;
  }
</style>
