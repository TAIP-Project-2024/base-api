import random

import networkx as nx
from django.template.context_processors import static
from sentence_transformers import SentenceTransformer, util

from api.models.domain.networkx_graph_impl import NetworkxDiGraphImpl, NetworkxGraphImpl
from api.services.general.graph_service import GraphService

COMMUNITY_COLORS = [
    "#3C3ABF",
    "#86159A",
    "#004F8E",
    "#8F2C2E",
    "#980000",
    "#364A80",
    "#185B1B",
    "#3A5718",
    "#9C1341",
    "#065A4F"
]

class GraphFactory:

    @staticmethod
    def random_graph(n):
        graph = NetworkxDiGraphImpl(f"random{n}barabasi", nx.barabasi_albert_graph(n, int(n/1.5)))
        return graph

    @staticmethod
    def topics_similarity_based_graph(name, posts, similarities, t = 0):
        """
        Args:
            name: name for the graph
            similarities: a similarity matrix
            t: similarity threshold
            returns a list of lists of indices representing communities,
        """
        hairball = nx.Graph()

        edges_tuples = []
        for line in similarities.items():
            for value in line[1]:
                try:
                    if similarities[line[0]][value] > t and value != line[0]:
                            edges_tuples.append((line[0], value, similarities[line[0]][value]))
                except KeyError as ke:
                    print(1)
                    print(ke)
                    continue

        hairball.add_weighted_edges_from(edges_tuples)
        nx.set_node_attributes(hairball, posts)
        partitions = nx.community.louvain_communities(hairball)
        print(f'detected {len(partitions)} partitions')
        if len(partitions) > 10:
            raise Exception("provide more colors :)")

        for i, partition in enumerate(partitions):
            for node in partition:
                hairball.nodes[node]['color'] = COMMUNITY_COLORS[i]
                hairball.nodes[node]['community'] = i

        graph = NetworkxGraphImpl(name, hairball)

        return graph
    @staticmethod
    def create_comments_graph(graph_name, post_text, comments, base_size = 15):
        """
        Args
        : post {text, url}
        : comments an array of objects that have an id,
        a body and a sentiment rank
        {id, title, sentiment, group(0,1,2)}
        """
        groups = ["group_negative", "group_neutral", "group_positive"]
        colors = ["red", "gray", "green"]
        graph = nx.Graph()
        graph.add_node("post", title=post_text, url="url", size = 25, color = "yellow")
        graph.add_node("group_neutral", label="Neutral", color="gray", size = base_size)
        graph.add_node("group_negative", label="Negative", color="red", size = base_size)
        graph.add_node("group_positive", label="Positive", color="green", size = base_size)
        graph.add_edges_from([("post", "group_neutral"), ("post", "group_positive"), ("post", "group_negative")])
        n = {}
        print([e["sentiment"] for e in comments])
        for entry in comments:
            group = groups[round(entry["sentiment"])]
            color = colors[entry["sentiment"]]
            label = "score " + str(entry["score"])
            print(color)
            graph.add_node(entry["_id"],
                           title=entry["text"],
                           label = label,
                           color=color,
                           group=group,
                           size=base_size,
                           hidden=True)

            graph.add_edge(group, entry["_id"])
            try:
                n[group] += 1
            except Exception as e:
                n[group] = 0
        for group in groups:
            try:
                graph.nodes[group]['size']=n[group]+30
            except:
                pass # means no such members
        return NetworkxGraphImpl(graph_name, graph)


# node_ids = ['mtr', 'hpa', 'vip', 'uem', 'pbf', 'rwc', 'dtk', 'hdw', 'wuw', 'aem',
#              'ecm', 'rhv', 'pbs', 'bwa', 'yel', 'pwf', 'nbm', 'uxd', 'wis', 'zmv',
#              'otw', 'puk', 'sjr', 'lvh', 'vwv', 'jkt', 'flu', 'ghi', 'qui', 'wwn',
#              'tpb', 'irt', 'oge', 'amd', 'vfr', 'txz', 'ahc', 'cyt', 'fwl', 'pkr',
#              'ivk', 'dfj', 'jnk', 'cxw', 'mqm', 'wqr', 'sqp', 'iwb', 'gqz', 'vso',
#              'zyo', 'cao', 'xal', 'kgk', 'mua', 'vzy', 'rlt', 'mze', 'oxw', 'iur',
#              'ypi', 'cvk', 'zwb', 'qta', 'wrr', 'zgp', 'rfu', 'ipe', 'fid', 'rkk',
#              'xbi', 'hst', 'dfc', 'wai', 'edf', 'kzn', 'rhx', 'wug', 'wsl', 'aau',
#              'ddy', 'jqh', 'cln', 'okb', 'prd', 'bui', 'lqw', 'ork', 'qad', 'rct',
#              'lje', 'rwu', 'mrw', 'nvj', 'muh', 'tin', 'xmg', 'ddg', 'tgj', 'zlq']
#
# similarities = {id_: {id_: random.randint(1, 10) for id_ in node_ids} for id_ in node_ids}
# topics = {}
# for i in range(100):
#     id = node_ids[i]
#     topics[id] = {'title':f'topic {id}', 'url':f'https://networkx.org/documentation/stable/index.html'}
# print(topics)


# g = GraphFactory.topics_similarity_based_graph('cool_graph', topics, similarities)
# g.save()
# GraphService().save_graph(NetworkxGraphImpl("cool_graph"), False)
reddit_posts = [
    "What is the most life-changing book you've ever read?",
    "I just discovered this amazing trick for saving money, and I had to share it!",
    "Does anyone else feel like time is moving faster as they get older?",
    "My cat just knocked over my coffee... again.",
    "How do you stay productive when working from home?",
    "Am I the only one who thinks pineapple on pizza is actually pretty good?",
    "Can someone explain why people are so obsessed with this new TV show?",
    "I finally completed my first marathon, and I'm so proud of myself!",
    "What’s your go-to comfort movie when you’re feeling down?",
    "Why does no one talk about how hard it is to make new friends as an adult?",
    "I just cooked a perfect steak for the first time. It feels like a huge achievement!",
    "Do you ever feel like your pet understands you better than people do?",
    "What’s a small habit that has drastically improved your life?",
    "My boss just gave me a raise, and I can't believe it!",
    "I started journaling last month, and it's helped me so much with my mental health.",
    "What’s the best advice you've ever received?",
    "Does anyone else procrastinate so much they stress about procrastinating?",
    "This picture I took last weekend is one of the best I’ve ever captured. What do you think?",
    "What’s the one thing you wish you could tell your younger self?",
    "Why is learning to cook such an underrated skill?",
    "I built my first PC today! Here's a photo of the setup.",
    "How do you deal with imposter syndrome at work?",
    "I just adopted a puppy, and my heart is full. Here’s a photo!",
    "What’s the best way to organize a small apartment?",
    "Is it weird that I find cleaning my room super therapeutic?",
    "This weekend I tried something new, and it was both terrifying and amazing.",
    "Why does nobody talk about how exhausting being an introvert can be?",
    "I think I’ve finally found my new favorite hobby—woodworking!",
    "What’s your unpopular opinion about modern technology?",
    "How do you balance staying informed with avoiding doomscrolling?",
    "My morning routine has changed my entire outlook on life.",
    "I tried meal prepping for the first time, and I actually saved so much time this week.",
    "Why do people always underestimate how expensive weddings are?",
    "I need advice: how do you handle disagreements with close friends?",
    "What’s a skill you picked up during lockdown that you still use today?",
    "Am I the only one who feels guilty for taking breaks during the workday?",
    "This subreddit has helped me so much—thank you, everyone!",
    "What’s the most overrated food trend in your opinion?",
    "Why is finding the right work-life balance so hard?",
    "I spent the whole weekend playing this new video game, and I have zero regrets.",
    "What’s the most wholesome thing that’s happened to you recently?"
]
node_ids = range(40)

posts = {}
#mock:
for i in range(40):
    id = node_ids[i]
    posts[id] = {'title':reddit_posts[id], 'url':f'https://networkx.org/documentation/stable/index.html'}

# model = SentenceTransformer('all-MiniLM-L6-v2')
#
# embeddings = model.encode(reddit_posts, batch_size=16, convert_to_tensor=True)
# sim = util.cos_sim(embeddings, embeddings)
# similarities = {i: {j: sim[i][j].item()*10 for j in node_ids} for i in node_ids}
#
# g = GraphFactory.topics_similarity_based_graph('40_random_posts', posts, similarities)
# g.save()
# GraphService().save_graph(NetworkxGraphImpl("40_random_posts"), False)
#
