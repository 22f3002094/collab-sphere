<template>
    <div class="mb-4">
        <router-link to="/home" class="text-purple-600 hover:text-purple-800">
            &larr; Back to Home
        </router-link>
    </div>
    <div class="px-8 py-6 max-w-5xl mx-auto ">
        <!-- Back Button -->


        <!-- Project Title and Status -->
        <div v-if="project" class="border rounded-2xl p-6 mb-6 shadow-sm bg-purple-50">
            <div class="flex justify-center items-center gap-2 mb-4">
                <h1 class="text-3xl font-semibold text-black text-center">{{ project.title }}</h1>
                <span :class="[
                    'inline-block w-3 h-3 rounded-full',
                    project.status === 'open' ? 'bg-green-500' : 'bg-red-500'
                ]" :title="project.status"></span>
            </div>
            <div class="flex justify-center mb-2">
                <span v-if="project.created_by && !iAmAuthor" class="text-gray-800 flex items-center gap-1">
                    <UserIcon class="w-4 h-4" /> {{ project.created_by }}
                </span>
            </div>

            <!-- Project Description -->
            <div class="mb-6  mt-3">
                <p class="text-lg text-gray-700">{{ project.description }}</p>
            </div>


            <div class="flex flex-wrap items-center   text-sm text-gray-600 mb-4 gap-4">
                <!-- Categories -->
                <div class="flex items-center gap-2">
                    <Squares2X2Icon class="w-4 h-4" />
                    <span v-for="(cat, i) in project.categories" :key="i">
                        {{ cat }}<span v-if="i < project.categories.length - 1"> · </span>
                    </span>
                </div>

                <!-- Tags -->
                <div v-if="project.tags.length" class="flex items-center flex-wrap gap-2">
                    <TagIcon class="w-4 h-4" />
                    <span v-for="(tag, i) in project.tags" :key="i"
                        class="bg-violet-100 px-3 py-1 rounded-full text-xs text-purple-700">
                        {{ tag }}
                    </span>
                </div>
            </div>


            <!-- Project Actions -->
            <div class="flex gap-6 justify-between items-center pt-2">
                <div class="text-sm text-gray-500">
                    <span>{{ project.interests }} Interested</span>
                </div>

                <!-- Show buttons only if user is NOT the author -->
                <template v-if="!iAmAuthor">
                    <div v-if="project.interested_by_user" class="flex space-x-3">
                        <button class="bg-purple-600 text-white font-semibold text-sm px-3 py-1.5 rounded-md">
                            Marked as Interested
                        </button>
                    </div>
                    <div v-else class="flex space-x-3">
                        <button @click="show_interest"
                            class="bg-purple-600 text-white font-semibold text-sm px-3 py-1.5 rounded-md">
                            I'm Interested
                        </button>
                    </div>
                </template>
            </div>



        </div>
        <!-- Tabs -->
        <div class="flex space-x-6 border-b mb-6 text-sm font-medium text-gray-600">
            <button v-for="tab in tabs" :key="tab" @click="changeTab(tab)"
                :class="['pb-2', activeTab === tab ? 'border-b-2 border-black text-black' : 'hover:text-black']">
                {{ tab }}
            </button>
        </div>

        <!-- Notice Tab Content -->
        <div v-if="activeTab === 'Notice'">
            <div v-if="iAmAuthor" class="flex justify-end mb-4">
                <button @click="showForm = !showForm"
                    class="bg-purple-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-purple-700">
                    New Notice
                </button>
            </div>
            <div v-if="iAmAuthor && showForm" class="max-w-xl mb-6 mx-auto bg-white p-6 rounded-xl shadow space-y-4">
                <!-- Title Input -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
                    <input v-model="form.title" type="text" placeholder="Enter title"
                        class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500" />
                </div>

                <!-- Text Input -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Text</label>
                    <textarea v-model="form.content" rows="4" placeholder="Write your content..."
                        class="w-full border border-gray-300 px-4 py-2 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-purple-500"></textarea>
                </div>

                <!-- Dropdown -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Visibility</label>
                    <select v-model="form.visibility"
                        class="w-full border border-gray-300 px-4 py-2 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-purple-500">
                        <option value="public">Public</option>
                        <option value="private">Private</option>
                    </select>
                </div>

                <!-- Submit Button -->
                <div class="text-right">
                    <button @click="postnotice"
                        class="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 font-semibold">
                        Submit
                    </button>
                </div>
            </div> 
            <div v-if = "notices.length">
            <NoticeCard v-for="(n, index) in notices" :key="index" :notice="n" :author="iAmAuthor" />
            </div>
            <div v-else>
                <p class="text-gray-500 text-center">No notices yet. </p>
            </div>
        </div>

        <!-- Placeholder for Discussion Tab -->
        <!-- Discussion Section -->
        <div v-if="activeTab === 'Discussion'" class="space-y-4">
            <div v-if ="comments.length">
            <CommentComponent v-for="(comment, index) in comments" :key="index" :comment="comment" :index="index"
                @reply-added="handleReply" />
            </div>
            <div v-else>
                <p class="text-gray-500 text-center">No comments yet. Be the first to comment!</p>
            </div>
            <!-- Main comment input -->
            <div class="flex items-center space-x-2 mt-4">
                <input v-model="newComment" placeholder="write your comment"
                    class="border px-4 py-2 rounded-full w-full text-sm" />
                <button @click="addComment" class="text-purple-600 text-xl">➤</button>
            </div>
        </div>
        <div v-if="activeTab === 'Settings'" class="space-y-4">

            <ProjectSetting></ProjectSetting>
        </div>

    </div>
</template>

<script>
import { UserIcon, TagIcon, Squares2X2Icon } from '@heroicons/vue/24/outline';
import NoticeCard from '../components/NoticePost.vue'; // Adjust the path as necessary
import CommentComponent from '../components/CommentComp.vue'; // Adjust the path as necessary
import ProjectSetting from '@/components/ProjectSetting.vue';
export default {
    name: 'ProjectDetail',
    data() {
        return {
            tabs: ['Notice', 'Discussion'],
            activeTab: 'Notice',
            project: null,
            notices: [],
            comments: [],
            newComment: '',
            form: {
                title: '',
                content: '',
                visibility: 'public'
            },
            showForm: false
        };
    },
    components: {
        UserIcon,
        TagIcon,
        Squares2X2Icon,
        NoticeCard,
        CommentComponent,
        ProjectSetting


    },
    computed: {
        iAmAuthor() {
            const user = JSON.parse(localStorage.getItem("user"));
            return this.project && user && this.project.created_by === user.name;
        }
    },
    async mounted() {
        // Fetch project data when the component is created
        const projectName = this.$route.params.slug; // Assuming the project name is passed as a route param
        try {
            const res = await fetch(`http://localhost:5000/api/project/${projectName}`);
            if (res.status === 401) {
                console.error('Unauthorized access. Please log in.');
                this.$router.push('/signin');
                return;
            }
            if (res.ok) {
                this.project = await res.json();
                console.log(this.project);
                if (localStorage.getItem("user")) {
                    const user = JSON.parse(localStorage.getItem("user"));
                    if (this.project.created_by === user.name) {
                        this.tabs = ['Notice', 'Discussion', "Settings"];
                    }
                }
                this.fetchNotices();

            } else {
                console.error("Failed to fetch project");
            }
        } catch (err) {
            console.error("Error fetching project:", err);
        }
    },

    methods: {
        changeTab(tab) {
            this.activeTab = tab;
            if (tab === 'Notice') {
                this.fetchNotices();
            }
            else if (tab === 'Discussion') {
                this.fetchComments();
            }
        },

        async show_interest() {
            const projectslug = this.$route.params.slug;
            try {
                const res = await fetch(`http://localhost:5000/api/utilities?action=showinterest&slug=${projectslug}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': `${localStorage.getItem("authtoken")}`
                    }
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    this.project.interested_by_user = true;
                    this.project.interests += 1;
                } else {
                    console.error("Failed to mark interest");
                }
            } catch (err) {
                console.error("Error marking interest:", err);
            }
        },
        async fetchNotices() {
            const projectslug = this.$route.params.slug;
            try {
                const res = await fetch(`http://localhost:5000/api/utilities?slug=${projectslug}&action=fetchnotices`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': `${localStorage.getItem("authtoken")}`
                    }
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    const d = await res.json();
                    this.notices = d.notices;
                    console.log(this.notices)
                } else {
                    console.error("Failed to fetch notices");
                }
            } catch (err) {
                console.error("Error fetching notices:", err);
            }
        },
        async fetchComments() {
            const slug = this.$route.params.slug;
            try {
                const res = await fetch(`http://localhost:5000/api/comments?slug=${slug}`, {
                    headers: {
                        'Authentication-Token': localStorage.getItem("authtoken")
                    }
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    const data = await res.json();
                    this.comments = data.comments;
                } else {
                    console.error("Failed to fetch comments");
                }
            } catch (err) {
                console.error("Error fetching comments:", err);
            }
        },
        async addComment() {
            const slug = this.$route.params.slug;
            if (!this.newComment.trim()) return;
            try {
                const res = await fetch(`http://localhost:5000/api/comments?slug=${slug}`, {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': localStorage.getItem("authtoken")
                    },
                    body: JSON.stringify({ text: this.newComment })
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    this.newComment = '';
                    await this.fetchComments(); // Refresh comment list
                }
            } catch (err) {
                console.error("Error adding comment:", err);
            }
        },

        async postnotice() {
            const projectslug = this.$route.params.slug;
            try {
                const res = await fetch(`http://localhost:5000/api/utilities?action=postnotice&slug=${projectslug}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': `${localStorage.getItem("authtoken")}`
                    },
                    body: JSON.stringify(this.form)
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    this.showForm = false;
                    this.form.title = '';
                    this.form.text = '';
                    this.form.visibility = 'public';
                    await this.fetchNotices();
                } else {
                    console.error("Failed to post notice");
                }
            } catch (err) {
                console.error("Error posting notice:", err);
            }
        }
        ,
        async handleReply({ commentIndex, reply }) {
            const commentId = this.comments[commentIndex].id;
            try {
                const res = await fetch(`http://localhost:5000/api/replies/${commentId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': localStorage.getItem("authtoken")
                    },
                    body: JSON.stringify({ text: reply.text })
                });
                if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                    return;
                }
                if (res.ok) {
                    await this.fetchComments(); // Refresh all comments including replies
                }
            } catch (err) {
                console.error("Error posting reply:", err);
            }
        }


    }
};
</script>

<style scoped>
button:focus {
    outline: none;
}
</style>