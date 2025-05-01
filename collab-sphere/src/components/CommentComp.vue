<template>
    <div class="w-full mb-4 p-4 border rounded-xl bg-white shadow">
        <!-- Main Comment -->
        <div class="flex items-start space-x-3">
            <UserCircleIcon class="w-10 h-10 rounded-full text-purple" alt="User" />
            <div class="flex-1">
                <div class="text-left text-gray-700 font-semibold text-base font-hand mb-1">
                    {{ comment.text }}
                </div>
                <div class="flex items-center space-x-2 text-sm text-gray-600">
                    <span class="font-semibold">{{ comment.username }}</span>
                    <span class="text-xs text-gray-400">• {{ comment.timestamp }}</span>
                </div>
            </div>

            <!-- Toggle Icon -->
            <!-- <button @click="toggleReplies" class="ml-auto text-purple-500 hover:text-purple-700">
                <ChatBubbleLeftEllipsisIcon v-if="!showReplies" class="h-5 w-5" />
                <XMarkIcon v-else class="h-5 w-5" />
            </button> -->
        </div>

        <!-- Replies Section -->
        <div v-if="showReplies" class="mt-5 flex flex-col items-center space-y-2 w-full">
            <div v-for="(reply, index) in comment.replies" :key="index"
                class="flex items-start space-x-3  w-full max-w-xl ">
                <div class="w-10 h-10 rounded-full bg-gray-300"></div>
                <div>
                    <div class="text-left text-gray-700 font-semibold text-base font-hand mb-1">{{ reply.text }}</div>
                    <div class="flex items-center space-x-2 text-sm text-gray-600">
                    <span class="font-semibold">{{ reply.username }}</span>
                    <span class="text-xs text-gray-400">• 2 hours ago</span>
                </div>
                    
                </div>
            </div>
            <!-- <div class="flex-1">
                <div class="text-left text-gray-700 font-semibold text-base font-hand mb-1">
                    {{ comment.text }}
                </div>
                <div class="flex items-center space-x-2 text-sm text-gray-600">
                    <span class="font-semibold">{{ comment.username }}</span>
                    <span class="text-xs text-gray-400">• {{ comment.timestamp }}</span>
                </div>
            </div> -->
            <!-- Reply Input -->
            <div class="mt-3 flex items-center space-x-2 w-1/2 max-w-xl">
                <input v-model="newReply" placeholder="write your reply"
                    class="border px-3 py-1.5 rounded-full w-full text-sm font-hand" />
                <button @click="submitReply" class="text-purple-600 hover:text-purple-800 text-xl">➤</button>
            </div>
        </div>

    </div>
</template>

<script>
// import { ChatBubbleLeftEllipsisIcon, XMarkIcon } from '@heroicons/vue/24/outline';
import { UserCircleIcon } from '@heroicons/vue/24/solid'

export default {
    name: 'CommentComponent',
    props: {
        comment: Object,
        index: Number
    },
    components: {
        
        UserCircleIcon
    },
    data() {
        return {
            showReplies: false,
            newReply: ''
        };
    },
    methods: {
        toggleReplies() {
            this.showReplies = !this.showReplies;
        },
        submitReply() {
    if (this.newReply.trim()) {
        this.$emit('reply-added', {
            commentIndex: this.index,
            reply: {
                text: this.newReply
            }
        });
        this.newReply = '';
    }
}


    }
};
</script>

<style scoped>
input:focus {
    outline: none;
}
</style>