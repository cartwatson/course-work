package com.jcarterw.usucsapp3.ui.research

class ResearchTopic(val title: String, val desc: String, val staff: String) {
    companion object {
        fun createResearchList() : ArrayList<ResearchTopic> {
            val ResearchTopics = ArrayList<ResearchTopic>()
            // Hard code faculty list
            ResearchTopics.add(ResearchTopic(
                "Artificial Intelligence",
                "Multi-agent systems, physics informed deep learning, criticality in natural systems, automatic differentiation, deep neural networks, AI for social impact, robotics, decision science, precision apiculture, precision agriculture, assistive technology, PIV/PTV, and computability.",
                "Faculty: Vicki Allan, Nick Flann, Hamid Karimi, Mario Harper, and Vladimir Kulyukin"))
            ResearchTopics.add(ResearchTopic(
                "Algorithms",
                "Planning algorithms, optimization algorithms, simulation, and computational geometry.",
                "Faculty: John Edwards, Mario Harper, and Haitao Wang"))
            ResearchTopics.add(ResearchTopic(
                "Augment Virtual Reality",
                "3D user interfaces, human perception and cognition in VR and AR.",
                "Faculty: Isaac Cho"))
            ResearchTopics.add(ResearchTopic(
                "Computer Science Education",
                "Educational data mining, keystroke analysis, and educational psychology.",
                "Faculty: John Edwards"))
            ResearchTopics.add(ResearchTopic(
                "Computer Vision",
                "Computer vision, pattern recognition, breast ultrasound (BUS) image processing, pavement crack detection/classification, uncertainty theories & new logics,  meta-learning, deep learning for medical Information processing, medical image segmentation, deep learning-based object detection & recognition, morphed face detection,  graph-based deep learning, and machine learning.",
                "Faculty: Hengda Cheng and Xiaojun Qi"))
            ResearchTopics.add(ResearchTopic(
                "Cybersecurity",
                "Human aspects of security, and privacy perceptions of users.",
                "Faculty: Mahdi Nasrullah Al-Ameen"))
            ResearchTopics.add(ResearchTopic(
                "Data Science and Data Mining",
                "Applied data mining for space weather research and pattern discovery from large time series data, social network analysis, graph mining, social media mining, educational data mining, machine learning, deep learning, representation learning of graphs and multivariate time series, ML cyberinfrastructure development, deep learning and its applications in anomaly detection, and natural language processing.",
                "Faculty: Soukaina Filali Boubrahimi, Hamid Karimi, Shah Muhammad Hamdi, and Shuhan Yuan"))
            ResearchTopics.add(ResearchTopic(
                "Data Visualization and Visual Analytics",
                "Decision-making and sense making, user behavior analytics, text analytics, and data analytics.",
                "Faculty: Isaac Cho"))
            ResearchTopics.add(ResearchTopic(
                "Database Systems",
                "Temporal databases, hierarchical databases, and biodiversity databases.",
                "Faculty: Curtis Dyreson"))
            ResearchTopics.add(ResearchTopic(
                "High Performance Computing and Scientific Visualization",
                "Big data analysis and visualization, distributed and parallel computing, topological analysis, cyberinfrastructure, cloud computing, and simulation visualization.",
                "Faculty:  John Edwards, Steve Petruzza"))
            return ResearchTopics
        }
    }
}