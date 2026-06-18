<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>전시원 병해충 실시간 모니터링 시스템</title>
    <!-- SheetJS (엑셀 다운로드용 라이브러리) -->
    <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
    <style>
        body { font-family: 'Malgun Gothic', sans-serif; margin: 20px; background-color: #f5f7f8; color: #333; }
        h1 { color: #2c3e50; text-align: center; }
        .container { max-width: 1000px; margin: 0 auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-bottom: 20px; }
        input, select, button { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; }
        button { background-color: #27ae60; color: white; border: none; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #219653; }
        .btn-excel { background-color: #2980b9; margin-bottom: 10px; float: right; }
        .btn-excel:hover { background-color: #2471a3; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; background: white; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #f2f2f2; color: #2c3e50; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .clear { clear: both; }
    </style>
</head>
<body>

<div class="container">
    <h1>🐛 병해충 예찰 실시간 공유 시스템</h1>
    
    <!-- 데이터 입력 폼 -->
    <div class="form-group">
        <input type="date" id="pestDate" required>
        <select id="investigator">
            <option value="">조사자 선택</option>
            <option value="김수림">김수림</option>
            <option value="주임님">주임님</option>
        </select>
        <input type="text" id="location" placeholder="발견 위치 (예: 만병초원)" required>
        <input type="text" id="pestName" placeholder="병해충명 (예: 미국선녀벌레)" required>
        <input type="text" id="memo" placeholder="특이사항 및 메모">
        <button onclick="submitData()">실시간 등록</button>
    </div>

    <hr>

    <!-- 엑셀 다운로드 버튼 -->
    <button class="btn-excel" onclick="downloadExcel()">📊 현재까지 데이터 엑셀 다운로드</button>
    <div class="clear"></div>

    <!-- 실시간 데이터 출력 테이블 -->
    <table>
        <thead>
            <tr>
                <th>날짜</th>
                <th>조사자</th>
                <th>위치</th>
                <th>병해충명</th>
                <th>특이사항</th>
            </tr>
        </thead>
        <tbody id="pestTableBody">
            <!-- 실시간으로 데이터가 여기에 쌓입니다 -->
        </tbody>
    </table>
</div>

<!-- Firebase 모듈 및 실시간 동기화 스크립트 -->
<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
    import { getFirestore, collection, addDoc, query, orderBy, onSnapshot } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

    // 수림님의 실제 파이어베이스 설정값 연동
    const firebaseConfig = {
        apiKey: "AIzaSyDrMCDQOUcKLuiGy4_X8CqrKvSqnxfmGV0",
        authDomain: "pest-monitoring-14e79.firebaseapp.com",
        projectId: "pest-monitoring-14e79",
        storageBucket: "pest-monitoring-14e79.firebasestorage.app",
        messagingSenderId: "247600445978",
        appId: "1:247600445978:web:5f89dd356c4daf73d2afa3"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    const pestCollection = collection(db, "pest_records");

    document.getElementById('pestDate').value = new Date().toISOString().substring(0, 10);

    window.submitData = async function() {
        const date = document.getElementById('pestDate').value;
        const investigator = document.getElementById('investigator').value;
        const location = document.getElementById('location').value;
        const pestName = document.getElementById('pestName').value;
        const memo = document.getElementById('memo').value;

        if (!date || !investigator || !location || !pestName) {
            alert("조사자, 위치, 병해충명은 필수 입력 항목입니다.");
            return;
        }

        try {
            await addDoc(pestCollection, {
                date: date,
                investigator: investigator,
                location: location,
                pestName: pestName,
                memo: memo,
                timestamp: new Date()
            });
            
            document.getElementById('location').value = '';
            document.getElementById('pestName').value = '';
            document.getElementById('memo').value = '';
        } catch (e) {
            console.error("데이터 추가 에러: ", e);
            alert("등록에 실패했습니다.");
        }
    }

    const q = query(pestCollection, orderBy("date", "desc"), orderBy("timestamp", "desc"));
    onSnapshot(q, (querySnapshot) => {
        const tbody = document.getElementById('pestTableBody');
        tbody.innerHTML = ''; 
        
        window.currentData = []; 

        querySnapshot.forEach((doc) => {
            const data = doc.data();
            window.currentData.push({
                '날짜': data.date,
                '조사자': data.investigator,
                '위치': data.location,
                '병해충명': data.pestName,
                '특이사항': data.memo
            });

            const row = `<tr>
                <td>${data.date}</td>
                <td>${data.investigator}</td>
                <td>${data.location}</td>
                <td>${data.pestName}</td>
                <td>${data.memo || ''}</td>
            </tr>`;
            tbody.innerHTML += row;
        });
    });

    window.downloadExcel = function() {
        if (!window.currentData || window.currentData.length === 0) {
            alert("다운로드할 데이터가 없습니다.");
            return;
        }
        const worksheet = XLSX.utils.json_to_sheet(window.currentData);
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, "병해충조사기록");
        
        const today = new Date().toISOString().substring(0, 10);
        XLSX.writeFile(workbook, `병해충_조사기록_취합_${today}.xlsx`);
    }
</script>

</body>
</html>
