<div align="center">

<img src="./assets/header.svg" width="100%" alt="Senthan Amuthan" />

<a href="https://senthan.vercel.app/">
  <img src="./assets/typing.svg" alt="Typing intro" />
</a>

<p>
  <a href="https://senthan.vercel.app/"><img src="./assets/badges/portfolio-senthan-vercel-app-lg.svg" alt="Portfolio" /></a>
  <img src="./assets/badges/based-in-chennai-india-lg.svg" alt="Chennai, India" />
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
      <img src="./assets/badges/java-sm.svg" />
      <img src="./assets/badges/spring-boot-sm.svg" />
      <img src="./assets/badges/apache-kafka-sm.svg" />
      <img src="./assets/badges/postgresql-sm.svg" />
      <img src="./assets/badges/docker-sm.svg" />
      <img src="./assets/badges/prometheus-sm.svg" />
      <img src="./assets/badges/grafana-sm.svg" />
      <img src="./assets/badges/jaeger-sm.svg" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/Hornet">Hornet</a></h4>
      <sub>Adaptive AI-driven deception platform</sub>
      <p>Mirrors a production network into an isolated digital twin (QEMU/KVM + Cowrie), redirects hostile traffic into it, adapts decoys with a PPO policy and emits STIX 2.1 indicators.</p>
      <img src="./assets/badges/python-sm.svg" />
      <img src="./assets/badges/qemu-kvm-sm.svg" />
      <img src="./assets/badges/reinforcement-learning-sm.svg" />
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/Minimal-Network-Lab">Minimal Network Lab</a></h4>
      <sub>On-demand VM lab orchestration</sub>
      <p>Spin up, access, stop and wipe isolated QEMU VMs from a Next.js dashboard, with in-browser VNC through a containerized Guacamole gateway.</p>
      <img src="./assets/badges/next-js-sm.svg" />
      <img src="./assets/badges/node-js-sm.svg" />
      <img src="./assets/badges/docker-sm.svg" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/OSINT">PhishGraph</a></h4>
      <sub>Automated phishing investigation</sub>
      <p>Takes a suspicious URL, domain or IP, enriches it across six intel providers, builds an infrastructure graph, scores risk with explainable factors and clusters findings into campaigns.</p>
      <img src="./assets/badges/python-sm.svg" />
      <img src="./assets/badges/osint-sm.svg" />
      <img src="./assets/badges/threat-intel-sm.svg" />
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/senthan-07/TeamFlow">TeamFlow</a> · <a href="https://team-flow-frontend.vercel.app/login">Live</a></h4>
      <sub>Real-time collaborative workspace</sub>
      <p>Shared boards with live drawing, chat, file sharing and WebRTC calls, synced over JWT-authenticated Socket.IO namespaces and persisted through Prisma on PostgreSQL in a Turborepo monorepo.</p>
      <img src="./assets/badges/next-js-sm.svg" />
      <img src="./assets/badges/socket-io-sm.svg" />
      <img src="./assets/badges/webrtc-sm.svg" />
      <img src="./assets/badges/postgresql-sm.svg" />
    </td>
  </tr>
</table>

---

<div align="center">

<img src="./assets/tech-stack.svg" width="100%" alt="Tech stack: Java, Go, TypeScript, Python, C++, Kotlin, Bash, Spring, Kafka, Node.js, Express, FastAPI, PostgreSQL, MongoDB, Prisma, Docker, Linux, Nix, Prometheus, Grafana, GitHub Actions, Git, React, Next.js, Tailwind" />

</div>

---

<div align="center">

<img width="100%" alt="Contribution graph as an arcade level, with repositories ranked as high scores" src="https://raw.githubusercontent.com/senthan-07/senthan-07/output/arcade.svg" />

</div>

---

<div align="center">

**Open to internships and collaborations in backend, distributed systems and infrastructure.**

<a href="https://senthan.vercel.app/"><img src="./assets/badges/get-in-touch-lg.svg" alt="Get in touch" /></a>

<img src="./assets/footer.svg" width="100%" alt="" />

</div>
