.<template>
    <div>
        <form @submit.prevent="submit_url">
            <input value="" id="surl" type="text" placeholder="Enter your url" v-model="message"/>
            <button type="submit" @click="submit_url" >Submit</button>
        </form>


    </div>
</template>

<script>
const url = "http://127.0.0.1:5000/api/data/"
export default {
    name: 'Form',
    data () {
        return {
            message: '',
        }
    },
    methods:{
      async submit_url(){

        const res = await fetch(url+this.message, {
            method:'POST',
            headers: { 'Content-Type': 'application/json' },
             })
        const data =  await res.json()
        console.log(data)

        },
    }

}
</script>

<style lang="scss" scoped>

</style>