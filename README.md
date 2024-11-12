![venom](https://capsule-render.vercel.app/api?type=venom&height=200&text=플레이데이터%20DE%2032기%20Team_Project_5rd%202조&fontSize=40&color=100:ff7f00,100:87ceeb&stroke=ffffff)

---

## 🫂 Team

|           역할            |                    이름[GitHub 주소]                    |                                   담당 업무                          |
|:-------------------------:|:-------------------------------------------------------:|:--------------------------------------------------------------------:|
|         예능 부장         | **김동욱** [[GitHub]](https://github.com/DONGUK777)     |   |
|  형상 및 배포 책임자(AA)  | **김도현** [[GitHub]](https://github.com/rlaehgus97)    |   |
|       기술 리더(TL)       | **이상우** [[GitHub]](https://github.com/GITSangWoo)    |   |
|       애자일 코치(AC)     | **이상훈** [[GitHub]](https://github.com/hun0219)       |   |
|            PM             | **조하영** [[GitHub]](https://github.com/EstherCho-7)   |   |

<br/>

### 🛠️활용 기술 스택
---
![Ubuntu](https://img.shields.io/badge/ubuntu-orange?style=for-the-badge&logo=ubuntu)
![linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=linux)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

</br>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

<br/>

![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Exporter](https://img.shields.io/badge/Exporter-000000?style=for-the-badge&logo=linux&logoColor=white)

<br/>

### 🗓️ 전체 프로젝트 일정
> **프로젝트 일정 : 2024년 11월 11일 ~ 2024년 11월 13일(총 3일)**

<br/>

## 목차
 1. [📚프로젝트 개요](#프로젝트-개요)
 2. [📋요구사항 정의서](#요구사항-정의서)
 3. [📅개발 일정](#개발-일정)
 4. [⚙주요 기능](#주요-기능)
 5. [🏗️시스템 아키텍처](#시스템-아키텍처)
 6. [🌐환경 구성](#환경-구성)
 7. [✅테스트 결과](#테스트-결과)
 8. [⌨트러블 슈팅 및 PR](#트러블-슈팅-및-PR)
 9. [🔄회고(KPT)](#회고(KPT))
10. [🔍최종 검토 및 개선](#최종-검토-및-개선)

<br/>

### 📚프로젝트 개요

#### Kubernetes & Docker 기반 웹 서버 모니터링 프로젝트

이 프로젝트는 Kubernetes 환경에서 Grafana와 Prometheus를 통해 웹 서버의 CPU 사용량을 실시간으로 모니터링하기 위한 설정을 포함합니다.
웹 서버는 docker compose up을 통해 컨테이너로 웹 서버가 배포되며, 부하 테스트를 통해 CPU 사용량 변화를 확인할 수 있습니다.

---
#### 프로젝트 시나리오
**[목적]**
> Kubernetes 환경에서 Prometheus와 Grafana를 사용하여 Docker 웹 서버의 CPU 사용량을 모니터링

**[구성요소]**
> **Docker 웹 서버**: CPU 부하를 발생시킬 웹 서버 Docker 컨테이너
> **Node Exporter**: Docker 컨테이너의 CPU 정보를 받아오기 위한 Exporter
> **Prometheus**: Kubernetes 클러스터와 애플리케이션의 메트릭 수집
> **Grafana**: Prometheus 메트릭을 기반으로 시각화 및 모니터링

**[주요 기능]**
> 웹 서버에 부하를 주어 CPU 사용량 변화 모니터링
> Grafana 대시보드를 통해 CPU 사용량을 시각화

<br/>

### 📋요구사항 정의서
---
#### 시스템 요구사항

| **요구사항 ID** | **구분**          | **요구사항 설명**                                                | **중요도** | **난이도** | **구현 상태** |
|:---------------:|:-----------------:|:----------------------------------------------------------------:|:----------:|:----------:|:-------------:|
| SYS-01          | 시스템 구성       | Grafana와 Prometheus를 Kubernetes에 배포                         | 높음       | 보통       | 완료          |
| SYS-02          | 모니터링 설정     | Prometheus가 Node Exporter를 통해 CPU 메트릭 수집                | 높음       | 보통       | 완료          |
| SYS-03          | 시각화 대시보드   | Grafana에서 CPU 사용량을 시각화하는 대시보드 구성               | 높음       | 보통       | 완료          |

#### 애플리케이션 기능 요구사항

| **요구사항 ID** | **구분**          | **요구사항 설명**                                                | **중요도** | **난이도** | **구현 상태** |
|:---------------:|:-----------------:|:----------------------------------------------------------------:|:----------:|:----------:|:-------------:|
| APP-01          | CPU 부하 발생     | 부하 테스트를 통해 Docker 웹 서버의 CPU 사용량을 증가시키기      | 높음       | 보통       | 완료          |
| APP-02          | 실시간 모니터링   | Grafana에서 실시간으로 CPU 사용량 변화 확인                     | 높음       | 보통       | 완료          |


<br/>

### 📅개발 일정
---
- [Git Hub 칸반보드]()

<br/>

### ⚙주요 기능
---
#### 1. Prometheus와 Grafana 배포
   - Kubernetes에 Prometheus와 Grafana를 설치하여 시스템 메트릭(예: CPU 사용량)을 수집하고 시각화합니다.
   
#### 2. Docker로 웹 서버 배포 및 부하 테스트
   - Docker Compose로 웹 서버를 실행하고 부하를 발생시켜 CPU 사용량의 변화를 관찰합니다.
   
#### 3. Grafana 대시보드에서 CPU 사용량 시각화
   - Prometheus에서 수집한 CPU 사용량 데이터를 Grafana 대시보드를 통해 실시간으로 모니터링합니다.

<br/>

### 🏗️시스템 아키텍처
---

<br/>

### 🌐환경 구성
---

<br/>

### ✅테스트 결과
---

<br/>

## ⌨트러블 슈팅 및 PR

<br/>

# 🔄회고(KPT)

## 김동욱
<details>
<summary>KEEP</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>PROBLEM</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
 </figure>
</div>
</details>


<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
 </figure>
</div>
</details>

## 김도현
<details>
<summary>KEEP</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>PROBELM</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

## 이상우
<details>
<summary>KEEP</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>PROBLEM</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

## 이상훈
<details>
<summary>KEEP</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>PROBLEM</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p></p>
 </figure>
</div>
</details>

## 조하영
<details>
<summary>KEEP</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>PROBLEM</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
  <p></p>
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p></p>
  <p></p>
 </figure>
</div>
</details>

<br/>

## 🔍최종 검토 및 개선


