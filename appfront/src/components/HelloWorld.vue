<template>


            <div class="row navb">
              <div class="img-circle circle img-responsive">
                <img :src="img" class="img-responsive img"/>
              </div>
              <div>
                <p class="tim">
                  <span class="glyphicon glyphicon-calendar date"></span><span id="date"></span>
                  <span class="glyphicon glyphicon-time time"></span><span id="time"></span>
                </p>
                <p class="tips">欢迎使用五舟科技硬件测试平台</p>
              </div>
            <ul class="nav nav-pills nav-stacked">
              <li role="presentation" @click="toggle()" :class="{active:open}">
                <router-link to="/"><span class="glyphicon glyphicon-home icon-img"></span>数据显示</router-link>
              </li>
              <li role="presentation" @click="toggle_two()" :class="{active:open_two}">
                <router-link :to="{name:'search'}"><span class="glyphicon glyphicon-search icon-img"></span>查看历史</router-link>
              </li>

            </ul>
            </div>


</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      img:'../static/image/logo.gif',
      open:true,
      open_two:false
    }
  },
  methods:{
    toggle:function(){
      this.open=true;
      this.open_two=false
    },
    toggle_two:function () {
      this.open_two=true;
      this.open=false;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
   .navb {

    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    /*right: 0;*/
    margin: auto;
    height: auto;

    padding-left: 0;
    padding-right: 0;
    padding-bottom: 0;
    text-align: center;
    background-color: rgba(48, 51, 60, 0);
  }
  .navb{
    background-color: #4A4949;
    height: 100%;

  }
  .tim{
    color: white;
    margin:0 1em .5em 1em;
    height: 2.5em;
    border-radius: .5em;
    background-color: #989898;

  }
  .date{
    line-height: 2.2em;
    margin: 0 .5em 0 1em;
  }
  .time{
    line-height: 2em;
    margin: 0 .5em 0 .5em;
  }
  .tips{
    color: white;
    text-align: center;
  }
  .circle{
    background-color: #242323;
    margin: 2em 3.3em 1em 3.3em;
    height: 9em;
  }
  @media (min-width: 1440px) and (max-width: 2560px){
    .circle{
      height: 15em;
    }
  }
  .img{
    width: 80%;
    height: 100%;
    margin: 0 auto;
  }
  @media screen and (max-width: 768px){
    .img{
      width: 100%;
      height: 90%;
    }
    .circle{
      margin: 1em;
    }

  }
  @media (min-width: 768px) and (max-width: 1024px) {
    .circle{
      margin: 1.5em;
    }
    .tim{
      margin:0 1em .5em 1em;
      height:4em;
    }
    .date{
      margin: 0 .5em 0 .5em;
    }
    .tips{
      font-size: .7em;
    }
  }


  .nav-pills>li>a{
    color: white;
  }
  .icon-img{
    margin-right: 1em;
  }

</style>
