<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:161b22,100:1f6feb&height=180&section=header&text=Senthan%20Amuthan&fontSize=46&fontColor=ffffff&fontAlignY=38&desc=Distributed%20Systems%20%E2%80%A2%20Backend%20%E2%80%A2%20Security&descAlignY=60&descSize=16" width="100%" alt="Senthan Amuthan" />

<a href="https://senthan.vercel.app/">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=3200&pause=900&color=58A6FF&center=true&vCenter=true&width=620&lines=Building+scalable%2C+fault-tolerant+systems;Distributed+storage+%C2%B7+Infrastructure+%C2%B7+Security;Designed+to+scale.+Built+to+survive+failure." alt="Typing intro" />
</a>

<p>
  <a href="https://senthan.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-senthan.vercel.app-1f6feb?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  <img src="https://img.shields.io/badge/Based%20in-Chennai%2C%20India-161b22?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Chennai, India" />
</p>

</div>

---

### About

I'm a **B.Tech Computer Science (Cyber Security)** student at **Shiv Nadar University**, Chennai. I build **scalable backend and distributed systems**: services that stay fast under load, recover on their own when parts fail, and are secure by design.

- **Distributed systems:** chunked storage, replication, self-healing repair, event-driven services on Kafka
- **Infrastructure:** QEMU/KVM virtualization, containerized environments, observability with Prometheus, Grafana and Jaeger
- **Security:** adaptive deception networks, OSINT-driven threat investigation, IOC enrichment

---

### Featured Work

<table>
  <tr>
    <td colspan="2" valign="top">
      <h3><a href="https://github.com/Gokul-Nishandh/AstraStore">AstraStore</a></h3>
      <sub>S3-style distributed object store, built from scratch · lead contributor</sub>
      <p>Files are split into 8 MiB chunks and streamed to storage nodes in constant memory, so a 4 GB upload uses the same RAM as a 4 KB one. Each chunk is replicated across nodes over Kafka events. A heartbeat state machine (<code>HEALTHY → DEGRADED → DOWN → RECOVERING</code>) drives rate-limited self-healing repair. The platform ships as microservices for gateway, auth, upload, placement, replication, metadata and storage, with SDKs for Java, Node and Python, plus full tracing and metrics.</p>
      <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
      <img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" />
      <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" />
      <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" />
      <img src="https://img.shields.io/badge/Jaeger-60D0E4?style=flat-square&logo=jaeger&logoColor=black" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/Hornet">Hornet</a></h4>
      <sub>Adaptive AI-driven deception platform</sub>
      <p>Mirrors a production network into an isolated digital twin (QEMU/KVM + Cowrie), redirects hostile traffic into it, adapts decoys with a PPO policy and emits STIX 2.1 indicators.</p>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/QEMU%2FKVM-FF6600?style=flat-square&logo=qemu&logoColor=white" />
      <img src="https://img.shields.io/badge/Reinforcement%20Learning-6E40C9?style=flat-square" />
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/Minimal-Network-Lab">Minimal Network Lab</a></h4>
      <sub>On-demand VM lab orchestration</sub>
      <p>Spin up, access, stop and wipe isolated QEMU VMs from a Next.js dashboard, with in-browser VNC through a containerized Guacamole gateway.</p>
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/OSINT">PhishGraph</a></h4>
      <sub>Automated phishing investigation</sub>
      <p>Takes a suspicious URL, domain or IP, enriches it across six intel providers, builds an infrastructure graph, scores risk with explainable factors and clusters findings into campaigns.</p>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/OSINT-0d1117?style=flat-square" />
      <img src="https://img.shields.io/badge/Threat%20Intel-B60205?style=flat-square" />
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/drawsync">DrawSync</a></h4>
      <sub>Real-time collaborative canvas</sub>
      <p>An infinite whiteboard where teams sketch, diagram and brainstorm together live, with shapes, text and freehand tools.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" />
    </td>
  </tr>
</table>

---

### Tech Stack

<div align="center">

**Languages**<br/>
<img src="https://skillicons.dev/icons?i=java,go,ts,py,cpp,kotlin,bash&theme=dark" alt="Languages" />

**Backend & Distributed Systems**<br/>
<img src="https://skillicons.dev/icons?i=spring,nodejs,express,fastapi,kafka,postgres,mongodb&theme=dark" alt="Backend and distributed systems" />

**Infrastructure & Observability**<br/>
<img src="https://skillicons.dev/icons?i=docker,linux,prometheus,grafana,git,github&theme=dark" alt="Infrastructure and observability" />

**Frontend**<br/>
<img src="https://skillicons.dev/icons?i=react,nextjs,tailwind&theme=dark" alt="Frontend" />

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/senthan-07/senthan-07/output/profile-night-view.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/senthan-07/senthan-07/output/profile-green.svg" />
  <img width="100%" alt="3D contribution graph" src="https://raw.githubusercontent.com/senthan-07/senthan-07/output/profile-night-view.svg" />
</picture>

<img src="https://streak-stats.demolab.com?user=senthan-07&hide_border=true&background=0d1117&ring=1f6feb&fire=58a6ff&currStreakLabel=58a6ff&sideLabels=c9d1d9&currStreakNum=ffffff&sideNums=ffffff&dates=8b949e&stroke=30363d" alt="GitHub streak" />

</div>

---

<div align="center">

**Open to internships and collaborations in backend, distributed systems and infrastructure.**

<a href="https://senthan.vercel.app/"><img src="https://img.shields.io/badge/Get%20in%20touch-1f6feb?style=for-the-badge&logo=maildotru&logoColor=white" alt="Get in touch" /></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,50:161b22,100:0d1117&height=110&section=footer" width="100%" alt="" />

</div>
