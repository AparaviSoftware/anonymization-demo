# Aparavi Pipeline Demo

AI-powered document processing with parsing, classification, and PII anonymization.

![Pipeline Visualization](./images/pipeline.png)

## 🚀 Quick Start

### 1. Get your API key
- **US customers**: [dtc.aparavi.com/usage](https://dtc.aparavi.com/usage)
- **EU customers**: [dtc.aparavi.eu/usage](https://dtc.aparavi.eu/usage)

### 2. Setup (one-time)

**Option A: Automated setup**
```bash
cd aparavi-pipeline-demo
python setup.py
```

**Option B: Manual setup**
```bash
cd aparavi-pipeline-demo
copy env.example .env   # Windows (or cp env.example .env on Mac/Linux)
```

Edit `.env` and add your API key:
```env
APARAVI_API_KEY=your-api-key-here
APARAVI_BASE_URL=https://eaas-dev.aparavi.com/
```

### 3. Run the demo

Open the Jupyter notebook:
```bash
jupyter notebook notebooks/demo.ipynb
```

Run all cells to see:
- ✅ Document parsing with AI
- ✅ PII detection and classification
- ✅ Automated text anonymization

## 📚 Learn More

- **Website**: [aparavi.com](https://aparavi.com)
- **SDK Documentation**: [GitHub](https://github.com/AparaviSoftware/aparavi-dtc-sdk)
- **Support**: support@aparavi.com

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using Aparavi Data Toolchain SDK**