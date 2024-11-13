![venom](https://capsule-render.vercel.app/api?type=venom&height=200&text=플레이데이터%20DE%2032기%20Team_Project_5rd%202조&fontSize=40&color=100:ff7f00,100:87ceeb&stroke=ffffff)

---

## 🫂 Team

| 역할                     | 이름         | 책임                                                         |
|--------------------------|--------------|--------------------------------------------------------------|
| **PM**                   | **조하영**    |  - 프로젝트 진행 상황 모니터링 및 관리<br> - 각 역할 간 커뮤니케이션 조율<br> - 프로젝트 일정 및 리소스 관리<br> - 팀 내외부와의 의사소통 및 문제 해결 |
| **애자일 코치 (AC)**      | **이상훈**    |  - 팀원들의 애로 사항 논의 및 해결 지원<br> - 애자일 프로세스 적용 및 지속적인 개선 지원<br> - 스프린트 계획 및 회고 관리 |
| **기술 리더 (TL)**       | **이상우**    |  - 기술적 문제 해결 및 방향 설정<br> - 시스템 아키텍처 설계 및 리뷰<br> - 기술적 결정을 내리고 팀원들에게 가이드 제공<br> - 코드 품질 관리 및 코드 리뷰 |
| **형상 및 배포 책임자 (AA)** | **김도현**    |  - Docker, Kubernetes 등 배포 환경 설정 및 관리<br> - 형상 관리 및 배포 관련 문제 해결<br> - 서비스 안정성 및 성능 모니터링 |
| **예능 부장**            | **김동욱**    |  - 팀 분위기 조성 및 팀원들의 고충 나누기<br> - 팀의 동기 부여 및 유대감 강화<br> - 팀 내 소통 및 협업을 위한 환경 조성 |


<br/>

### 🛠️활용 기술 스택
---
![Ubuntu](https://img.shields.io/badge/ubuntu-orange?style=for-the-badge&logo=ubuntu)
![linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=linux)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

<br>

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Exporter](https://img.shields.io/badge/Exporter-000000?style=for-the-badge&logo=linux&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017E9A?style=for-the-badge&logo=apache-airflow&logoColor=white)

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

#### Kubernetes & Docker 기반 웹 서버 모니터링 및 오토스케일링 프로젝트

이 프로젝트는 Kubernetes와 Docker를 활용하여 웹 서버의 CPU 사용량을 실시간으로 모니터링하고, 부하 발생 시 서버가 자동으로 스케일링하도록 구성하는 것이 목표입니다.
또한, 예상 부하 증가 시 관리자 페이지를 통해 수동으로 서버를 확장할 수 있는 기능을 제공합니다.

+ 추가 기능

파이널 프로젝트를 대비해 추후 설계될 구조를 시뮬레이션 할 수 있게 구현하였다.

#### 프로젝트 시나리오
**[목적]**
> Kubernetes에서 Prometheus와 Grafana를 사용하여 Docker 웹 서버의 CPU 사용량을 모니터링하고, 자동 및 수동 스케일링을 통해 부하에 유연하게 대응하는 시스템 구축.

**[구성요소]**
> **Docker 웹 서버**: CPU 부하를 발생시킬 웹 서버 Docker 컨테이너
> **Node Exporter**: Docker 컨테이너의 CPU 정보를 받아오기 위한 Exporter
> **Prometheus**: Kubernetes 클러스터와 애플리케이션의 메트릭 수집
> **Grafana**: Prometheus 메트릭을 기반으로 시각화 및 모니터링
> **Streamlit 관리자 페이지**: 예상 부하 증가 시 수동 스케일링을 지원하는 관리 기능

Step.2
> **AirFlow**: 파이널 프로젝트에서 크롤링 한 데이터를 ETL 하기 위한 프레임 워크
> **Spark**: 파이널 프로젝트에서 생길 대용량 데이터를 병렬 처리 하기 위한 프레임 워크 


**[주요 기능]**
> 웹 서버에 부하를 주어 CPU 사용량 변화 모니터링
> Grafana 대시보드를 통해 CPU 사용량을 시각화
> 이벤트 대비를 위한 수동 스케일 업/다운 기능이 있는 관리자 페이지 제공

<br/>

### 📋요구사항 정의서
---
#### 1. 기능적 요구사항

| **요구사항 ID** | **구분**            | **요구사항 설명**                                                                                          | **중요도** | **구현 상태** |
|-----------------|---------------------|------------------------------------------------------------------------------------------------------------|------------|---------------|
| **FR-01**           | 모니터링            | 웹 서버의 CPU 사용량을 실시간으로 모니터링하고 Grafana에서 시각화할 수 있어야 한다.                        | 높음       | 완료          |
| **FR-02**           | 자동 스케일링       | CPU 사용량이 임계값을 초과하면 자동으로 Kubernetes에서 스케일 업/다운을 해야 한다.                         | 높음       | 완료          |
| **FR-03**           | 수동 스케일링       | Streamlit 관리자 페이지에서 수동으로 스케일 업/다운을 할 수 있어야 한다.                                   | 중간       | 완료          |
| **FR-04**           | 부하 테스트         | Docker Compose로 웹 서버를 배포하고, 설정된 부하에 따른 CPU 사용량 변화를 테스트할 수 있어야 한다.         | 중간       | 완료          |
| **FR-05**           | 데이터 수집 및 변환 | 최종 프로젝트에서 크롤링할 데이터를 수집하고 변환할 수 있어야 한다.                                        | 중간       | 미완료        |
| **FR-06**           | 데이터 분산 처리    | 최종 프로젝트에서 받아올 데이터를 Scale in/out을 통해 데이터를 분산 처리할 수 있어야 한다.                 | 높음       | 미완료        |

#### 2. 비기능적 요구사항

| **요구사항 ID** | **구분**     | **요구사항 설명**                                                                                             | **중요도** | **구현 상태** |
|-----------------|--------------|---------------------------------------------------------------------------------------------------------------|------------|---------------|
| **NFR-01**          | 성능         | 시스템은 웹 서버에 부하가 발생해도 성능 저하 없이 안정적으로 작동해야 한다.                                   | 높음       | 완료          |
| **NFR-02**          | 확장성       | 웹 서버는 트래픽이 증가할 때 자동으로 스케일링되어야 하며, 시스템 성능이 유지되어야 한다.                     | 높음       | 완료          |
| **NFR-03**          | 안정성       | 자동 및 수동 스케일링 기능이 정상적으로 동작하고, 장애 발생 시 서비스가 중단되지 않아야 한다.                 | 높음       | 완료          |

#### 3. 제약 사항

| **요구사항 ID** | **구분**     | **요구사항 설명**                                                                                             | **중요도** | **구현 상태** |
|----------------|---------------|---------------------------------------------------------------------------------------------------------------|------------|---------------|
| **CR-01**          | 기술 스택     | Kubernetes, Prometheus, Grafana, Docker Compose, Streamlit 등 지정된 기술 스택을 사용해야 한다.               | 높음       | 완료          |
| **CR-02**          | 환경 설정     | 시스템은 로컬 및 클라우드(Kubernetes) 환경에서 모두 동작해야 한다.                                            | 높음       | 완료          |

#### 4. 구현 상태

| **구분**   | **구현 상태**         | **설명**                                |
|------------|-----------------------|-----------------------------------------|
| **완료**       | 전체 시스템           | 모든 기능이 정상적으로 동작하고 있음    |
| **완료**       | 스케일링              | 자동 및 수동 스케일링 기능 완료         |
| **완료**       | 부하 테스트           | 부하 테스트가 정상적으로 동작함         |
| **미완료**     | 데이터 수집 및 변환   | 데이터를 수집 및 변환하는 동작은 구현 X |
| **미완료**     | 데이터 분산 처리      | 데이터 분산처리 기능 동작 X             |

<br/>

### 📅개발 일정
---
- [Git Hub 칸반보드]()

<br/>

### ⚙주요 기능
---
#### 1. Kubernetes 상의 Prometheus 및 Grafana 배포
   - Kubernetes 클러스터에 Prometheus와 Grafana를 배포하여 웹 서버의 CPU 사용량을 수집하고 대시보드에서 실시간으로 확인합니다.

#### 2. Docker 웹 서버 배포 및 부하 테스트
   - Docker Compose로 웹 서버를 실행하고, 부하 테스트를 통해 CPU 사용량 변화를 관찰합니다.

#### 3. 자동 및 수동 스케일링
   - **자동 스케일링**: CPU 사용량이 설정된 임계치를 넘으면 서버가 자동으로 스케일 업됩니다.
   - **수동 스케일링**: 관리자 페이지에서 필요에 따라 수동으로 서버 스케일 업/다운을 조정할 수 있습니다.

<br/>

### 🏗️시스템 아키텍처
---
![image](https://github.com/user-attachments/assets/5d35abed-b4a5-4c5f-aee8-60cdabac13ae)

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
  <p>- 새로 배운 것을 프로젝트에 적용해본다는 점에서 의미 깊었다.</p>
 </figure>
</div>
</details>

<details>
<summary>PROBLEM</summary>
<div>
<figure align="center">
  <p> 코드에서의 문제가 없었으나 실행이 되지 않는 이유를 코드에서만 찾는 경향이 있다.</p>
 </figure>
</div>
</details>

<details>
<summary>TRY</summary>
<div>
<figure align="center">
  <p>- 문법 이슈 외에 다른 환경설정 사항들도 고려해볼 것</p>
 </figure>
</div>
</details>

<br/>

## 🔍최종 검토 및 개선


